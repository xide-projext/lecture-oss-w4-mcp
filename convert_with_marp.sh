#!/bin/bash

# Marp가 설치되어 있는지 확인
if ! command -v marp &> /dev/null; then
    echo "Marp CLI가 설치되어 있지 않습니다. 설치가 필요합니다."
    echo "npm install -g @marp-team/marp-cli"
    exit 1
fi

# docs 디렉토리 확인 및 생성
if [ ! -d "docs" ]; then
    mkdir docs
fi

# 슬라이드 파일 변환
for file in MCP_강의자료_슬라이드*.md; do
    echo "변환 중: $file"
    marp --html --output docs/$(basename "${file%.*}").html "$file"
done

# 실습 가이드 변환
for file in MCP_강의자료_실습가이드.md MCP_커스텀서버_개발가이드.md README.md; do
    if [ -f "$file" ]; then
        echo "변환 중: $file"
        marp --html --output docs/$(basename "${file%.*}").html "$file"
    fi
done

# 예제 코드 html로 변환
for pyfile in *.py; do
    if [ -f "$pyfile" ]; then
        basename="${pyfile%.*}"
        echo "Python 파일 변환 중: $pyfile"
        cat > "docs/${basename}.html" << EOL
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${pyfile}</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/styles/default.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/highlight.min.js"></script>
    <script>hljs.highlightAll();</script>
    <style>
        body { 
            font-family: 'Noto Sans KR', sans-serif; 
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            max-width: 1200px;
            margin: 0 auto;
        }
        pre { 
            background-color: #f5f5f5; 
            padding: 15px; 
            border-radius: 5px; 
            overflow-x: auto;
        }
        .container {
            background-color: white;
            padding: 30px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        nav { margin-bottom: 20px; }
        nav a { margin-right: 15px; }
    </style>
</head>
<body>
    <div class="container">
        <nav>
            <a href="index.html">홈</a>
            <a href="슬라이드목록.html">슬라이드</a>
            <a href="MCP_강의자료_실습가이드.html">실습 가이드</a>
        </nav>
        <h1>${pyfile}</h1>
        <pre><code class="language-python">
$(cat "${pyfile}")
        </code></pre>
    </div>
</body>
</html>
EOL
    fi
done

# 인덱스 페이지 생성
cat > "docs/index.html" << EOL
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MCP(Model Context Protocol) 강의 자료</title>
    <style>
        body { 
            font-family: 'Noto Sans KR', sans-serif; 
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            max-width: 1200px;
            margin: 0 auto;
        }
        .container {
            background-color: white;
            padding: 30px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        h1 { color: #2c3e50; }
        h2 { color: #3498db; border-bottom: 1px solid #eee; padding-bottom: 10px; }
        ul { list-style-type: square; }
        a { color: #3498db; text-decoration: none; }
        a:hover { text-decoration: underline; }
        .section { margin-bottom: 30px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>MCP(Model Context Protocol) 강의 자료</h1>
        
        <div class="section">
            <h2>슬라이드 자료</h2>
            <ul>
                <li><a href="MCP_강의자료_슬라이드1-3.html">슬라이드 1-3: MCP의 개요</a></li>
                <li><a href="MCP_강의자료_슬라이드4-6.html">슬라이드 4-6: MCP의 오픈소스화와 구조</a></li>
                <li><a href="MCP_강의자료_슬라이드7-9.html">슬라이드 7-9: MCP의 영향과 활용</a></li>
                <li><a href="MCP_강의자료_슬라이드10-12.html">슬라이드 10-12: 개발 생산성과 실습 개요</a></li>
                <li><a href="MCP_강의자료_슬라이드13-15.html">슬라이드 13-15: Git 연동과 코드 실행</a></li>
                <li><a href="MCP_강의자료_슬라이드16-18.html">슬라이드 16-18: 테스트 자동화와 미래 전망</a></li>
                <li><a href="MCP_강의자료_슬라이드19-21.html">슬라이드 19-21: MCP 도입 고려사항과 결론</a></li>
                <li><a href="MCP_강의자료_슬라이드22-24.html">슬라이드 22-24: MCP 서버 및 클라이언트 실습</a></li>
                <li><a href="MCP_강의자료_슬라이드25-27.html">슬라이드 25-27: GitHub 연동과 추가 학습 자료</a></li>
            </ul>
        </div>
        
        <div class="section">
            <h2>실습 가이드 및 예제 코드</h2>
            <ul>
                <li><a href="MCP_강의자료_실습가이드.html">MCP 실습 가이드</a></li>
                <li><a href="MCP_커스텀서버_개발가이드.html">MCP 커스텀 서버 개발 가이드</a></li>
                <li><a href="MCP_파이썬서버_예제코드.html">MCP 파이썬 서버 예제 코드</a></li>
                <li><a href="MCP_클라이언트_사용예제.html">MCP 클라이언트 사용 예제</a></li>
            </ul>
        </div>
        
        <div class="section">
            <h2>프로젝트 문서</h2>
            <ul>
                <li><a href="README.html">README (프로젝트 개요)</a></li>
            </ul>
        </div>
    </div>
</body>
</html>
EOL

# 슬라이드 목록 페이지 생성
cat > "docs/슬라이드목록.html" << EOL
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MCP 강의 슬라이드 목록</title>
    <style>
        body { 
            font-family: 'Noto Sans KR', sans-serif; 
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            max-width: 1200px;
            margin: 0 auto;
        }
        .container {
            background-color: white;
            padding: 30px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        h1 { color: #2c3e50; }
        ul { list-style-type: none; padding: 0; }
        li { 
            margin-bottom: 15px; 
            padding: 15px;
            background-color: #f8f9fa;
            border-radius: 5px;
            transition: background-color 0.3s;
        }
        li:hover { background-color: #e9ecef; }
        a { 
            color: #3498db; 
            text-decoration: none;
            display: block;
            font-weight: bold;
            font-size: 1.1em;
        }
        .description {
            color: #6c757d;
            margin-top: 5px;
        }
        nav { margin-bottom: 20px; }
        nav a { margin-right: 15px; }
    </style>
</head>
<body>
    <div class="container">
        <nav>
            <a href="index.html">홈</a>
            <a href="MCP_강의자료_실습가이드.html">실습 가이드</a>
        </nav>
        
        <h1>MCP 강의 슬라이드 목록</h1>
        
        <ul>
            <li>
                <a href="MCP_강의자료_슬라이드1-3.html">슬라이드 1-3: MCP의 개요</a>
                <div class="description">MCP의 정의와 필요성, MCP의 역사와 발전 과정, MCP의 오픈소스화 배경</div>
            </li>
            <li>
                <a href="MCP_강의자료_슬라이드4-6.html">슬라이드 4-6: MCP의 오픈소스화와 구조</a>
                <div class="description">오픈소스화가 개발자 및 산업에 미친 영향, MCP의 기본 아키텍처, 주요 컴포넌트와 역할</div>
            </li>
            <li>
                <a href="MCP_강의자료_슬라이드7-9.html">슬라이드 7-9: MCP의 영향과 활용</a>
                <div class="description">다양한 산업 분야에서의 MCP 적용 사례, MCP의 확산 과정과 현재의 위치, MCP와 AI 도구를 활용한 차세대 코딩</div>
            </li>
            <li>
                <a href="MCP_강의자료_슬라이드10-12.html">슬라이드 10-12: 개발 생산성과 실습 개요</a>
                <div class="description">개발 생산성 향상 사례, 실습 목표와 필요 사항, MCP 환경 설정</div>
            </li>
            <li>
                <a href="MCP_강의자료_슬라이드13-15.html">슬라이드 13-15: Git 연동과 코드 실행</a>
                <div class="description">Git 및 GitHub 연동, MCP를 활용한 Git 워크플로우, 코드 실행 및 테스트</div>
            </li>
            <li>
                <a href="MCP_강의자료_슬라이드16-18.html">슬라이드 16-18: 테스트 자동화와 미래 전망</a>
                <div class="description">테스트 자동화 심화, 패키지 관리와 배포, MCP의 미래 전망</div>
            </li>
            <li>
                <a href="MCP_강의자료_슬라이드19-21.html">슬라이드 19-21: MCP 도입 고려사항과 결론</a>
                <div class="description">MCP 도입 시 고려사항, 실습 데모, 요약 및 결론</div>
            </li>
            <li>
                <a href="MCP_강의자료_슬라이드22-24.html">슬라이드 22-24: MCP 서버 및 클라이언트 실습</a>
                <div class="description">Python으로 MCP 서버 구현, MCP 클라이언트 개발, MCP와 AI 모델 연동</div>
            </li>
            <li>
                <a href="MCP_강의자료_슬라이드25-27.html">슬라이드 25-27: GitHub 연동과 추가 학습 자료</a>
                <div class="description">GitHub MCP 서버 활용, 고급 MCP 사용 사례, 결론 및 추가 학습 자료</div>
            </li>
        </ul>
    </div>
</body>
</html>
EOL

echo "모든 파일이 docs/ 디렉토리에 변환되었습니다."
echo "GitHub Pages에서 확인하려면 저장소 설정에서 GitHub Pages 소스를 'docs' 폴더로 설정하세요."
