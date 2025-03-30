import javalang
import ollama
import streamlit as st


def read_java_file(uploaded_file):
    java_code = uploaded_file.read().decode('utf-8')  # Decode bytes to string
    return java_code
    

def parse_java_code(code):
    tree = javalang.parse.parse(code)
    class_info = {}
    
    for path, node in tree:
        if isinstance(node, javalang.tree.ClassDeclaration):
            class_info['name'] = node.name
            class_info['methods'] = []
            class_info['fields'] = []

            
        elif isinstance(node, javalang.tree.MethodDeclaration):
            
            method_details = {
                "name": node.name,
                "return_type": node.return_type.name if node.return_type else None,
                "parameters": [param.type.name + " " + param.name for param in node.parameters]
            }
            
            class_info['methods'].append(method_details)
            
                    
        elif isinstance(node, javalang.tree.FieldDeclaration):
            
            for declarator in node.declarators:
                class_info['fields'].append({
                    "name": declarator.name,
                    "type": node.type.name
                })
    
    return class_info

def generate_documentation(class_info):
    """Generates an easy-to-understand explanation using Ollama."""
    prompt = f"""Give me a brief explanation of the class 
                {class_info['name']}
                Explain it in a way that a beginner can understand."""
                
    response = ollama.chat(model="gemma:2b",
                           messages= [{"role": "user", "content": prompt}])
    
    return response['message']['content']




if __name__ == '__main__':
    print("Setting up things...")
    
    #java_code = read_java_file('Car.java')
    #class_info = parse_java_code(java_code)
    # documentation = generate_documentation(class_info)
    
    st.title('Java Doc Generator')
    uploaded_file = st.file_uploader("Upload a java file", type=["java"])
    
    if uploaded_file is not None:
        java_code = read_java_file(uploaded_file)
        class_info = parse_java_code(java_code)
        
        if st.button("Generate Documentation"):
            with st.spinner("Generating documentation..."):
                print("Generating documentation...")
                documentation = generate_documentation(class_info)
            st.success("Documentation generated successfully!")
            st.text_area("Generated Documentation", documentation, height=300)    