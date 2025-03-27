# MCP 커스텀 서버 개발 가이드

## 1. 개발 환경 설정

### 필요한 라이브러리 설치

#### Python 개발 환경
```bash
# 필수 라이브러리 설치
pip install model-context-protocol-python-sdk

# 개발용 도구 설치
pip install pytest pytest-asyncio black mypy
```

#### TypeScript/JavaScript 개발 환경
```bash
# MCP SDK 설치
npm install @modelcontextprotocol/sdk

# 개발용 도구 설치
npm install typescript ts-node eslint jest --save-dev
```

### 프로젝트 구조 설정

#### Python 프로젝트 구조
```
my-mcp-server/
├── server.py              # 메인 서버 코드
├── handlers/              # 기능별 핸들러
│   ├── __init__.py
│   ├── data_handlers.py
│   └── utility_handlers.py
├── tests/                 # 테스트 코드
│   ├── __init__.py
│   └── test_handlers.py
├── README.md              # 문서
├── requirements.txt       # 의존성 정의
└── setup.py               # 패키지 설정
```

#### TypeScript 프로젝트 구조
```
my-mcp-server/
├── src/
│   ├── server.ts          # 메인 서버 코드
│   ├── handlers/          # 기능별 핸들러
│   │   ├── index.ts
│   │   ├── dataHandlers.ts
│   │   └── utilityHandlers.ts
│   └── types.ts           # 타입 정의
├── tests/                 # 테스트 코드
│   └── handlers.test.ts
├── README.md              # 문서
├── package.json           # 의존성 및 스크립트
└── tsconfig.json          # TypeScript 설정
```

## 2. 서버 기본 구조 개발

### Python으로 MCP 서버 개발

```python
from model_context_protocol.server import MCPServer, Request, Response, register_handler

class MyCustomServer(MCPServer):
    """커스텀 MCP 서버 구현"""

    def __init__(self):
        super().__init__(
            name="my-custom-server",
            display_name="My Custom Server",
            description="Custom MCP server for specific domain needs",
            version="1.0.0",
        )
    
    @register_handler("example_handler")
    async def example_handler(self, request: Request) -> Response:
        """예제 핸들러 구현"""
        params = request.params
        
        # 요청 처리 로직 구현
        result = {"message": "Hello from MCP server!"}
        
        return Response(
            data=result,
            status="success"
        )

# 서버 실행
if __name__ == "__main__":
    server = MyCustomServer()
    server.start(host="localhost", port=3000)
    print("Custom MCP Server running on http://localhost:3000")
```

### TypeScript로 MCP 서버 개발

```typescript
import { MCPServer, Request, Response } from '@modelcontextprotocol/sdk';

class MyCustomServer extends MCPServer {
  constructor() {
    super({
      name: "my-custom-server",
      displayName: "My Custom Server",
      description: "Custom MCP server for specific domain needs",
      version: "1.0.0",
    });
    
    // 핸들러 등록
    this.registerHandler("example_handler", this.exampleHandler.bind(this));
  }
  
  async exampleHandler(request: Request): Promise<Response> {
    const params = request.params;
    
    // 요청 처리 로직 구현
    const result = { message: "Hello from MCP server!" };
    
    return {
      data: result,
      status: "success"
    };
  }
}

// 서버 실행
const server = new MyCustomServer();
server.start(3000, "localhost").then(() => {
  console.log("Custom MCP Server running on http://localhost:3000");
});
```

## 3. 핸들러 설계 및 구현

### 효과적인 핸들러 설계 원칙

1. **단일 책임**: 각 핸들러는 하나의 명확한 기능을 수행해야 함
2. **명확한 파라미터**: 필요한 파라미터를 명확히 정의하고 유효성 검사 수행
3. **일관된 응답 형식**: 성공 및 오류 응답의 일관된 구조 유지
4. **적절한 오류 처리**: 예상 가능한 오류를 식별하고 명확한 오류 메시지 제공

### 핸들러 구현 예시 (Python)

```python
@register_handler("get_data")
async def get_data(self, request: Request) -> Response:
    """데이터 조회 핸들러"""
    
    params = request.params
    data_id = params.get("id")
    
    # 파라미터 유효성 검사
    if not data_id:
        return Response(
            data={"error": "Data ID is required"},
            status="error"
        )
    
    try:
        # 데이터 조회 로직
        data = await self._fetch_data(data_id)
        
        return Response(
            data={"result": data},
            status="success"
        )
    except DataNotFoundError:
        return Response(
            data={"error": f"Data with ID {data_id} not found"},
            status="error"
        )
    except Exception as e:
        return Response(
            data={"error": f"Failed to fetch data: {str(e)}"},
            status="error"
        )
```

## 4. 보안 및 접근 제어

### 인증 및 권한 부여

```python
@register_handler("protected_data")
async def protected_data(self, request: Request) -> Response:
    """보안이 필요한 데이터 접근 핸들러"""
    
    # 인증 확인
    auth_token = request.headers.get("Authorization")
    if not auth_token or not self._validate_token(auth_token):
        return Response(
            data={"error": "Unauthorized access"},
            status="error",
            status_code=401
        )
    
    # 권한 확인
    user_id = self._get_user_from_token(auth_token)
    if not self._has_permission(user_id, "read_data"):
        return Response(
            data={"error": "Permission denied"},
            status="error",
            status_code=403
        )
    
    # 인증된 요청 처리
    # ...
```

### 데이터 접근 제한

- 경로 접근 제한 (파일 시스템 서버)
- 데이터베이스 쿼리 제한 (DB 서버)
- API 요청 제한 (외부 API 연동 서버)

## 5. 테스트 및 배포

### 서버 테스트 작성 (Python - pytest)

```python
import pytest
import json
from model_context_protocol.client import MCPClient

@pytest.mark.asyncio
async def test_example_handler():
    # 테스트용 클라이언트 생성
    client = MCPClient()
    await client.connect("http://localhost:3000")
    
    # 핸들러 호출
    response = await client.invoke("example_handler", {"param": "value"})
    
    # 응답 검증
    assert response.status == "success"
    assert "message" in response.data
    assert response.data["message"] == "Hello from MCP server!"
    
    await client.close()
```

### 서버 배포 옵션

1. **독립 실행 서비스**
   - systemd 서비스로 등록
   - Docker 컨테이너로 배포
   - Kubernetes 클러스터에 배포

2. **통합 배포**
   - 기존 애플리케이션 내 MCP 서버 기능 통합
   - 확장 가능한 플러그인 아키텍처 구현

3. **클라우드 서비스**
   - AWS Lambda, Google Cloud Functions 등으로 서버리스 배포
   - API Gateway와 통합

## 6. 고급 기능

### 스트리밍 응답 구현

```python
@register_handler("stream_data")
async def stream_data(self, request: Request) -> AsyncGenerator[Response, None]:
    """스트리밍 응답을 제공하는 핸들러"""
    
    params = request.params
    count = params.get("count", 5)
    
    for i in range(count):
        # 데이터 생성 또는 조회
        chunk_data = {"part": i + 1, "data": f"Chunk {i + 1} data"}
        
        yield Response(
            data=chunk_data,
            status="success",
            is_final=(i == count - 1)
        )
        
        # 처리 시간 시뮬레이션
        await asyncio.sleep(0.5)
```

### 다른 MCP 서버와의 통합

```python
async def _call_other_mcp_server(self, server_url, handler, params):
    """다른 MCP 서버 호출"""
    
    client = MCPClient()
    await client.connect(server_url)
    
    try:
        response = await client.invoke(handler, params)
        return response
    finally:
        await client.close()
```

## 7. 문서화 및 배포

### API 문서 생성

- 자동 문서 생성 도구 활용
- 핸들러 설명, 파라미터, 응답 형식 문서화
- 예제 코드 제공

### 배포 체크리스트

1. 모든 테스트 통과 확인
2. 코드 품질 검사 (linting, type checking)
3. 보안 취약점 점검
4. 성능 테스트
5. 문서 작성 완료
6. 버전 관리 및 변경 내역 작성