import os

from flask import Flask, request, jsonify

from third.document_service import read_documents_file, read_tags_file, get_documents_by_tag, \
    build_tag_names_to_tag_nodes

app = Flask(__name__)


@app.route('/taggedContent', methods=['GET'])
def get_tagged_content():
    tag = request.args.get('tag')
    if not tag:
        return jsonify({"error": "Tag is required"}), 400
    result_docs = get_documents_by_tag(documents_data, tag, tag_name_to_tag_node)

    return jsonify(result_docs)


if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    tags_data = read_tags_file(os.path.join(script_dir, 'tags.json'))
    documents_data = read_documents_file(os.path.join(script_dir, 'documents.json'))
    tag_name_to_tag_node = build_tag_names_to_tag_nodes(tags_data)
    app.run()
