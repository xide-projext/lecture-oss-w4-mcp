#!/usr/bin/env python3
"""
마크다운 파일을 HTML로 변환하는 스크립트
"""

import os
import re
import markdown
from pathlib import Path

# HTML 템플릿
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/styles/default.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/highlight.min.js"></script>
    <script>hljs.highlightAll();</script>
</head>
<body>
    <div class="container">
        <header>
            <h1>{title}</h1>
            <nav>
                <ul>
                    <li><a href="index.html">홈</a></li>
                    <li><a href="slides.html">모든 슬라이드</a></li>
                    <li><a href="practice.html">실습 가이드</a></li>
                    <li><a href="examples.html">예제 코드</a></li>
                </ul>
            </nav>
        </header>
        <main>
            {content}
        </main>
        <footer>
            <p>MCP(Model Context Protocol) 강의 자료 - 2025</p>
        </footer>
    </div>
</body>
</html>
"""

# CSS 파일 생성
CSS_CONTENT = """
/* 기본 스타일 */
body {
    font-family: 'Noto Sans KR', sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f8f9fa;
    margin: 0;
    padding: 0;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

header {
    background-color: #2c3e50;
    color: white;
    padding: 20px;
    border-radius: 5px 5px 0 0;
    margin-bottom: 20px;
}

header h1 {
    margin: 0;
    font-size: 2em;
}

nav ul {
    display: flex;
    list-style: none;
    padding: 0;
    margin: 10px 0 0 0;
}

nav ul li {
    margin-right: 20px;
}

nav ul li a {
    color: white;
    text-decoration: none;
    transition: color 0.3s;
}

nav ul li a:hover {
    color: #3498db;
}

main {
    background-color: white;
    padding: 30px;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

footer {
    text-align: center;
    margin-top: 20px;
    padding: 20px;
    color: #7f8c8d;
    font-size: 0.9em;
}

/* 슬라이드 스타일 */
.slide {
    border-bottom: 1px solid #eee;
    padding-bottom: 30px;
    margin-bottom: 30px;
}

.slide:last-child {
    border-bottom: none;
}

/* 코드 스타일 */
pre {
    background-color: #f5f5f5;
    padding: 15px;
    border-radius: 5px;
    overflow-x: auto;
}

code {
    font-family: 'Source Code Pro', monospace;
    font-size: 0.9em;
}

/* 버튼 및 링크 스타일 */
.btn {
    display: inline-block;
    padding: 10px 15px;
    background-color: #3498db;
    color: white;
    text-decoration: none;
    border-radius: 4px;
    transition: background-color 0.3s;
}

.btn:hover {
    background-color: #2980b9;
}

/* 반응형 디자인 */
@media (max-width: 768px) {
    .container {
        padding: 10px;
    }
    
    header, main {
        padding: 15px;
    }
    
    nav ul {
        flex-direction: column;
    }
    
    nav ul li {
        margin-bottom: 5px;
    }
}

/* 테이블 스타일 */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
}

table, th, td {
    border: 1px solid #ddd;
}

th, td {
    padding: 12px 15px;
    text-align: left;
}

th {
    background-color: #f2f2f2;
}

tr:nth-child(even) {
    background-color: #f8f8f8;
}

/* 특별 스타일 */
.highlight {
    background-color: #fffde7;
    padding: 20px;
    border-left: 4px solid #ffd600;
    margin: 20px 0;
}

.note {
    background-color: #e8f5e9;
    padding: 20px;
    border-left: 4px solid #43a047;
    margin: 20px 0;
}

.warning {
    background-color: #ffebee;
    padding: 20px;
    border-left: 4px solid #d32f2f;
    margin: 20px 0;
}
"""

# Python 코드를 HTML로 변환하는 함수
def convert_py_to_html(py_file_path, output_dir):
    with open(py_file_path, 'r', encoding='utf-8') as f:
        py_content = f.read()
    
    # 파일명 추출
    file_name = os.path.basename(py_file_path)
    output_name = os.path.splitext(file_name)[0] + '.html'
    
    # 코드를 HTML로 포맷팅
    html_content = f"<h1>{file_name}</h1>\n<pre><code class='python'>{py_content}</code></pre>"
    
    # HTML 템플릿에 삽입
    full_html = HTML_TEMPLATE.format(
        title=file_name,
        content=html_content
    )
    
    # HTML 파일 저장
    output_path = os.path.join(output_dir, output_name)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    return output_name

# 마크다운을 HTML로 변환하는 함수
def convert_md_to_html(md_file_path, output_dir):
    with open(md_file_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # 파일명 추출
    file_name = os.path.basename(md_file_path)
    output_name = os.path.splitext(file_name)[0] + '.html'
    
    # 마크다운을 HTML로 변환
    html_content = markdown.markdown(
        md_content,
        extensions=['extra', 'codehilite', 'tables', 'toc']
    )
    
    # 제목 추출 (첫 번째 h1 태그)
    title_match = re.search(r'<h1>(.*?)</h1>', html_content)
    title = title_match.group(1) if title_match else file_name
    
    # HTML 템플릿에 삽입
    full_html = HTML_TEMPLATE.format(
        title=title,
        content=html_content
    )
    
    # HTML 파일 저장
    output_path = os.path.join(output_dir, output_name)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    return output_name

# 슬라이드 파일들을 하나로 합치는 함수
def combine_slides(slide_files, output_dir):
    combined_content = "# MCP 강의 슬라이드 모음\n\n"
    
    # 슬라이드 파일 번호 순으로 정렬
    sorted_slides = sorted(slide_files, key=lambda x: int(re.search(r'슬라이드(\d+)-\d+', x).group(1)))
    
    