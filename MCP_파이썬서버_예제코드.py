"""
MCP(Model Context Protocol) 파이썬 서버 구현 예제

이 예제는 간단한 파일 시스템 액세스를 제공하는 MCP 서버를 구현합니다.
"""

from model_context_protocol.server import MCPServer, Request, Response, register_handler
import os
import json
from typing import Dict, List, Any


class FileSystemServer(MCPServer):
    """파일 시스템에 접근하는 MCP 서버 구현"""

    def __init__(self):
        super().__init__(
            name="filesystem",
            display_name="File System",
            description="Access and manage files and directories",
            version="1.0.0",
        )

    @register_handler("list_files")
    async def list_files(self, request: Request) -> Response:
        """디렉토리 내의 파일 목록을 반환합니다"""
        
        params = request.params
        path = params.get("path", ".")
        
        try:
            files = os.listdir(path)
            file_info = []
            
            for file in files:
                full_path = os.path.join(path, file)
                is_dir = os.path.isdir(full_path)
                
                file_info.append({
                    "name": file,
                    "type": "directory" if is_dir else "file",
                    "size": os.path.getsize(full_path) if not is_dir else None,
                })
            
            return Response(
                data={"files": file_info},
                status="success"
            )
        except Exception as e:
            return Response(
                data={"error": str(e)},
                status="error"
            )

    @register_handler("read_file")
    async def read_file(self, request: Request) -> Response:
        """파일 내용을 읽어 반환합니다"""
        
        params = request.params
        path = params.get("path")
        
        if not path:
            return Response(
                data={"error": "File path is required"},
                status="error"
            )
        
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            
            return Response(
                data={"content": content},
                status="success"
            )
        except Exception as e:
            return Response(
                data={"error": str(e)},
                status="error"
            )

    @register_handler("write_file")
    async def write_file(self, request: Request) -> Response:
        """파일에 내용을 작성합니다"""
        
        params = request.params
        path = params.get("path")
        content = params.get("content")
        
        if not path or content is None:
            return Response(
                data={"error": "File path and content are required"},
                status="error"
            )
        
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            
            return Response(
                data={"message": f"Successfully wrote to {path}"},
                status="success"
            )
        except Exception as e:
            return Response(
                data={"error": str(e)},
                status="error"
            )

    @register_handler("create_directory")
    async def create_directory(self, request: Request) -> Response:
        """새 디렉토리를 생성합니다"""
        
        params = request.params
        path = params.get("path")
        
        if not path:
            return Response(
                data={"error": "Directory path is required"},
                status="error"
            )
        
        try:
            os.makedirs(path, exist_ok=True)
            
            return Response(
                data={"message": f"Successfully created directory {path}"},
                status="success"
            )
        except Exception as e:
            return Response(
                data={"error": str(e)},
                status="error"
            )


# 서버 실행 코드
if __name__ == "__main__":
    server = FileSystemServer()
    server.start(port=3000)
    print("MCP File System Server running on port 3000")
