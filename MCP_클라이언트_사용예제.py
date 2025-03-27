"""
MCP(Model Context Protocol) 클라이언트 사용 예제

이 예제는 MCP 클라이언트를 사용하여 파일 시스템 MCP 서버에 연결하고 상호작용하는 방법을 보여줍니다.
"""

from model_context_protocol.client import MCPClient
import asyncio
import json


async def main():
    # MCP 클라이언트 생성
    client = MCPClient()
    
    # 서버 연결
    server_url = "http://localhost:3000"
    print(f"Connecting to MCP server at {server_url}...")
    
    try:
        await client.connect(server_url)
        print("Connected successfully!")
        
        # 서버 정보 확인
        server_info = await client.get_server_info()
        print(f"Server Info: {json.dumps(server_info, indent=2)}")
        
        # 사용 가능한 기능 목록 확인
        handlers = await client.list_handlers()
        print(f"Available handlers: {', '.join(handlers)}")
        
        # 현재 디렉토리 파일 목록 가져오기
        response = await client.invoke("list_files", {"path": "."})
        
        if response.status == "success":
            print("\nFiles in current directory:")
            for file in response.data["files"]:
                file_type = file["type"]
                file_name = file["name"]
                file_size = file["size"] if file["size"] is not None else "N/A"
                print(f"[{file_type.upper()}] {file_name} - Size: {file_size} bytes")
        else:
            print(f"Error listing files: {response.data.get('error')}")
        
        # 파일 읽기 예제
        file_name = "README.md"  # 읽을 파일 이름
        print(f"\nReading file: {file_name}")
        
        read_response = await client.invoke("read_file", {"path": file_name})
        
        if read_response.status == "success":
            print(f"File content:\n{read_response.data['content']}")
        else:
            print(f"Error reading file: {read_response.data.get('error')}")
        
        # 새 파일 작성 예제
        new_file = "example.txt"
        content = "This is a test file created using MCP."
        print(f"\nWriting to file: {new_file}")
        
        write_response = await client.invoke("write_file", {
            "path": new_file,
            "content": content
        })
        
        if write_response.status == "success":
            print(f"Successfully wrote to file: {new_file}")
        else:
            print(f"Error writing file: {write_response.data.get('error')}")
        
        # 새 디렉토리 생성 예제
        new_dir = "mcp_example_dir"
        print(f"\nCreating directory: {new_dir}")
        
        dir_response = await client.invoke("create_directory", {"path": new_dir})
        
        if dir_response.status == "success":
            print(f"Successfully created directory: {new_dir}")
        else:
            print(f"Error creating directory: {dir_response.data.get('error')}")
            
    except Exception as e:
        print(f"Error connecting to MCP server: {str(e)}")
    finally:
        # 연결 종료
        await client.close()
        print("\nConnection closed")


if __name__ == "__main__":
    asyncio.run(main())
