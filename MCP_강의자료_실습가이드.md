---
marp: true
---
# MCP(Model Context Protocol) 실습 가이드

## 1. MCP 환경 설정

### 필요한 도구 및 라이브러리 설치

1. **Claude Desktop 설치**
   - [Claude Desktop 다운로드 페이지](https://www.anthropic.com/claude-desktop)에서 운영체제에 맞는 버전 설치
   - 계정 생성 및 로그인

2. **Git MCP 서버 설정**
   - Git 설치 확인: `git --version`
   - Git MCP 서버 설치:
     ```bash
     npm install -g @modelcontextprotocol/git-server
     ```

3. **개발 환경 준비**
   - 선호하는 코드 에디터 준비 (VS Code 권장)
   - Node.js 및 npm 설치 확인

---

### 프로젝트 초기화 및 구성

1. **프로젝트 디렉토리 생성**
   ```bash
   mkdir mcp-demo-project
   cd mcp-demo-project
   ```

2. **MCP 서버 설정**
   ```bash
   # Git MCP 서버 실행
   mcp-git-server --port 3000
   ```

3. **Claude Desktop에 MCP 서버 연결**
   - Claude Desktop 실행
   - 설정 > MCP 서버 > 추가
   - 서버 URL 입력: `http://localhost:3000`


---

## 2. Git 및 GitHub 연동

### 로컬 저장소 생성 및 초기화

1. **Git 저장소 초기화**
   - Claude Desktop에서 다음 명령 입력:
     ```
     로컬 Git 저장소를 초기화해주세요.
     ```
   - Claude가 MCP를 통해 저장소 초기화:
     ```bash
     git init
     ```

2. **초기 파일 생성**
   - README.md 파일 생성:
     ```
     README.md 파일을 생성해주세요.
     ```

---

### 원격 저장소와의 연결 및 코드 푸시

1. **GitHub 저장소 생성**
   - GitHub 계정에 로그인
   - 새 저장소 생성 (mcp-demo-project)
   - HTTPS URL 복사

2. **로컬 저장소와 원격 저장소 연결**
   - Claude Desktop에서 다음 명령 입력:
     ```
     GitHub 저장소 URL: https://github.com/username/mcp-demo-project.git
     이 저장소를 origin으로 추가해주세요.
     ```

3. **변경사항 커밋 및 푸시**
   - Claude Desktop에서 다음 명령 입력:
     ```
     변경사항을 커밋하고 GitHub에 푸시해주세요.
     ```

---

## 3. 코드 실행 및 테스트

### MCP를 활용한 코드 실행 방법

1. **샘플 애플리케이션 작성**
   - Node.js 애플리케이션 초기화:
     ```
     Node.js 프로젝트를 초기화하고 간단한 웹 서버 코드를 작성해주세요.
     ```

2. **코드 실행**
   - Claude Desktop에서 다음 명령 입력:
     ```
     작성한 코드를 실행해주세요.
     ```
   - MCP를 통한 실행 결과 확인


---

### 테스트 작성 및 자동화

1. **테스트 프레임워크 설정**
   - Claude Desktop에서 다음 명령 입력:
     ```
     Jest 테스트 프레임워크를 설치하고 기본 테스트 코드를 작성해주세요.
     ```

2. **테스트 실행**
   - Claude Desktop에서 다음 명령 입력:
     ```
     작성한 테스트를 실행해주세요.
     ```

3. **테스트 결과 분석**
   - 테스트 결과 리포트 검토
   - 개선 사항 파악


---

## 4. 패키지 관리와 배포

### 의존성 관리 및 패키지 설치

1. **패키지 추가**
   - Claude Desktop에서 다음 명령 입력:
     ```
     Express와 Axios 패키지를 프로젝트에 추가해주세요.
     ```

2. **패키지 관리 최적화**
   - 패키지 의존성 검토:
     ```
     현재 프로젝트의 의존성을 검토하고 최적화해주세요.
     ```


---

### 프로젝트 빌드 및 배포 과정

1. **빌드 스크립트 생성**
   - package.json에 빌드 스크립트 추가:
     ```
     프로젝트 빌드 스크립트를 package.json에 추가해주세요.
     ```

2. **배포 준비**
   - .gitignore 및 환경 설정 파일 작성:
     ```
     배포를 위한 .gitignore 파일과 환경 설정 파일을 작성해주세요.
     ```

3. **배포 자동화**
   - GitHub Actions 워크플로우 작성:
     ```
     GitHub Actions를 사용하여 CI/CD 파이프라인을 설정해주세요.
     ```

---

## 5. MCP 활용 고급 기능

### 코드 분석 및 개선

1. **코드 리뷰 요청**
   - Claude Desktop에서 다음 명령 입력:
     ```
     현재 코드를 분석하고 개선점을 제안해주세요.
     ```

2. **성능 최적화**
   - Claude Desktop에서 다음 명령 입력:
     ```
     코드 성능을 최적화하는 방법을 제안해주세요.
     ```

---

### MCP 통합 확장

1. **추가 MCP 서버 연결**
   - 데이터베이스 MCP 서버 연결
   - 클라우드 서비스 MCP 서버 연결

2. **커스텀 MCP 서버 개발**
   - 프로젝트 특화 기능을 위한 커스텀 MCP 서버 개발 방향