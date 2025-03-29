import javalang
import ollama


def read_java_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    

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
                
    response = ollama.chat(model="mistral",
                           messages= [{"role": "user", "content": prompt}])
    
    return response['message']['content']

    
    

if __name__ == '__main__':
    print("Setting up things...")
    java_code = read_java_file('Car.java')
    class_info = parse_java_code(java_code)
    documentation = generate_documentation(class_info)