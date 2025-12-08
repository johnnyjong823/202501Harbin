import fitz  # PyMuPDF
import os

def extract_pdf_to_markdown(pdf_path, output_path):
    """從 PDF 提取文字並轉換為 Markdown 格式"""
    doc = fitz.open(pdf_path)
    
    markdown_content = []
    markdown_content.append("# 哈爾濱旅行行程\n")
    
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text()
        
        if text.strip():
            markdown_content.append(f"\n---\n## 第 {page_num + 1} 頁\n")
            markdown_content.append(text)
    
    doc.close()
    
    # 寫入 Markdown 檔案
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(markdown_content))
    
    print(f"已成功將 PDF 轉換為 Markdown: {output_path}")
    return '\n'.join(markdown_content)

if __name__ == "__main__":
    pdf_path = r"d:\Work\TestProject\產生旅行行程\inputs\哈爾濱.pdf"
    output_path = r"d:\Work\TestProject\產生旅行行程\docs\哈爾濱旅行行程.md"
    
    # 確保 docs 目錄存在
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    content = extract_pdf_to_markdown(pdf_path, output_path)
    print("\n=== 提取的內容預覽 ===\n")
    print(content[:5000])  # 只顯示前 5000 字元
