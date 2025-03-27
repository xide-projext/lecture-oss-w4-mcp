#!/usr/bin/env python3
"""
3개씩 나누어진 슬라이드 파일을 하나로 통합하는 스크립트
"""

import os
import re
import glob

def combine_slides():
    """슬라이드 파일들을 하나로 통합"""
    # 슬라이드 파일 경로
    slide_pattern = 'MCP_강의자료_슬라이드*.md'
    slide_files = glob.glob(slide_pattern)
    
    if not slide_files:
        print(f"슬라이드 파일을 찾을 수 없습니다: {slide_pattern}")
        return False
    
    # 슬라이드 번호 기준으로 정렬
    slide_files.sort(key=lambda x: int(re.search(r'슬라이드(\d+)-', x).group(1)))
    
    combined_content = """---
marp: true
theme: "theme.css"
paginate: true
header: Open Source Software Application (From Linux to LLM Openness)
footer: Seungwoo Hong Adjunct Professor / Spring Semester 2025 / Yonsei University
---
"""
    
    # 각 슬라이드 파일의 내용 통합
    for slide_file in slide_files:
        print(f"처리 중: {slide_file}")
        with open(slide_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Marp 헤더를 완전히 제거 (모든 형태 포함)
            content = re.sub(r'---\s*\nmarp:.*?(?:\n.*?)*?\n---', '', content)
            
            # 각 슬라이드 파일의 시작 부분에서 첫 번째 제목 라인 제거 (전체 슬라이드에서는 중복)
            content = re.sub(r'^# MCP.*?\n', '', content, 1)
            
            # 제목이 바로 시작되는 경우 (---\n# 형태) 처리
            content = content.lstrip()
            
            # 슬라이드 파일에 포함된 내용 추가하고 슬라이드 구분자 추가
            combined_content += content + "\n\n---\n\n"
    
    # 결과 파일 저장
    output_file = 'MCP_강의자료_전체슬라이드.md'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(combined_content)
    
    print(f"슬라이드 통합 완료: {output_file}")
    return True

if __name__ == "__main__":
    combine_slides()
