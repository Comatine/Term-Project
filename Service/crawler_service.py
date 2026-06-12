from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import json
import time
from typing import Dict, Any

class Crawler:
    """
    Selenium만 사용하는 크롤러
    장점: JavaScript 렌더링 지원, 동적 콘텐츠 처리 가능
    단점: 느림, 메모리 많이 사용
    """
    
    BASE_URL = "https://www.dekaron.co.kr/Board/ItemInfoView"
    
    @staticmethod
    def get_item_description(item_id: int, debug: bool = False, timeout: int = 15) -> Dict[str, Any]:
        """
        Selenium으로 아이템 정보 추출
        
        Args:
            item_id: 아이템 ID
            debug: 디버그 메시지 출력 여부
            timeout: 페이지 로드 대기 시간 (초)
        
        Returns:
            dict: 아이템 정보
        """
        url = f"{Crawler.BASE_URL}?itemIndex={item_id}"
        
        if debug:
            print(f"\n[Selenium] Starting item #{item_id}")
            print(f"[Selenium] URL: {url}")
            print(f"[Selenium] Method: Selenium WebDriver + JavaScript Rendering")
        
        item_info = {
            "title": "",
            "sections": [],
            "description": ""
        }
        
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
        
        driver = webdriver.Chrome(options=options)
        
        try:
            if debug:
                print("[Selenium] Loading page...")
            
            driver.get(url)
            
            # ==================== JavaScript 렌더링 대기 ====================
            try:
                wait = WebDriverWait(driver, timeout)
                
                # detail_wrap 대기
                wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'detail_wrap')))
                if debug:
                    print("[Selenium] ✓ detail_wrap found")
                
                # 콘텐츠 렌더링 대기
                time.sleep(2)
                
                wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'right')))
                if debug:
                    print("[Selenium] ✓ Content rendered")
                
                # 텍스트 로드 확인
                right_elements = driver.find_elements(By.CLASS_NAME, 'right')
                text_found = any(elem.text.strip() for elem in right_elements)
                
                if text_found:
                    if debug:
                        print("[Selenium] ✓ Text content loaded")
                else:
                    if debug:
                        print("[Selenium] ⚠ Warning: No text in right elements")
                
            except TimeoutException:
                print("[Selenium] ✗ Timeout waiting for content")
                return item_info
            
            # ==================== Selenium으로 직접 파싱 ====================
            try:
                # 타이틀 추출
                try:
                    title_elem = driver.find_element(By.CLASS_NAME, 'detail_title')
                    item_info["title"] = title_elem.text.strip()
                    if debug:
                        print(f"[Selenium] ✓ Title: {item_info['title']}")
                except Exception:
                    if debug:
                        print("[Selenium] ⚠ Title not found")
                
                # 섹션 추출
                section_elems = driver.find_elements(By.CLASS_NAME, 'detail_title')
                
                if debug:
                    print(f"[Selenium] Found {len(section_elems)} sections")
                
                for section_elem in section_elems:
                    section_title = section_elem.text.strip()
                    
                    current_section = {
                        "title": section_title,
                        "attributes": []
                    }
                    
                    if debug:
                        print(f"[Selenium] Processing: {section_title}")
                    
                    # 이 섹션 내의 데이터 찾기
                    try:
                        # 섹션 제목 요소의 부모 찾기
                        parent = section_elem.find_element(By.XPATH, "..")
                        
                        # 다음 형제 요소들에서 left/right 찾기
                        # JavaScript로 처리 (더 정확)
                        script = """
                        var titleElem = arguments[0];
                        var parent = titleElem.parentElement;
                        var results = [];
                        var current = titleElem.nextElementSibling;
                        
                        while(current) {
                            if (current.classList.contains('detail_title') || 
                                current.classList.contains('detail_bar')) {
                                break;
                            }
                            
                            var left = current.querySelector('.left');
                            var right = current.querySelector('.right');
                            
                            if (left && right) {
                                results.push({
                                    key: left.textContent.trim(),
                                    value: right.textContent.trim()
                                });
                            }
                            
                            current = current.nextElementSibling;
                        }
                        
                        return results;
                        """
                        
                        attributes = driver.execute_script(script, section_elem)
                        
                        for attr in attributes:
                            current_section["attributes"].append(attr)
                            if debug:
                                print(f"  {attr['key']}: {attr['value']}")
                    
                    except Exception as e:
                        if debug:
                            print(f"[Selenium] ⚠ Error extracting attributes: {e}")
                    
                    if current_section["attributes"]:
                        item_info["sections"].append(current_section)
                        if debug:
                            print(f"[Selenium] ✓ {len(current_section['attributes'])} attributes\n")
                
                # 설명 추출
                try:
                    detail_bars = driver.find_elements(By.CLASS_NAME, 'detail_bar')
                    
                    if len(detail_bars) >= 2:
                        script = """
                        var bar1 = arguments[0];
                        var bar2 = arguments[1];
                        var text = '';
                        var current = bar1.nextElementSibling;
                        
                        while(current && current !== bar2) {
                            var content = current.textContent.trim();
                            if (content) {
                                text += content + ' ';
                            }
                            current = current.nextElementSibling;
                        }
                        
                        return text.trim();
                        """
                        
                        description = driver.execute_script(script, detail_bars[0], detail_bars[1])
                        
                        if description:
                            item_info["description"] = description
                            if debug:
                                print(f"[Selenium] ✓ Description: {len(description)} chars")
                
                except Exception as e:
                    if debug:
                        print(f"[Selenium] ⚠ Error extracting description: {e}")
            
            except Exception as e:
                print(f"[Selenium] ✗ Error parsing content: {e}")
                import traceback
                traceback.print_exc()
        
        except Exception as e:
            print(f"[Selenium] ✗ Critical error: {e}")
            import traceback
            traceback.print_exc()
        
        finally:
            driver.quit()
            if debug:
                print("[Selenium] Browser closed\n")
        
        return item_info