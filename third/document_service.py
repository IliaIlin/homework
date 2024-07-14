import json

from first.gnode import GNode, walk_graph


def read_tags_file(filename):
    with open(filename, 'r') as tags_file:
        return json.load(tags_file)


def read_documents_file(filename):
    with open(filename, 'r') as documents_file:
        return json.load(documents_file)


def build_tag_names_to_tag_nodes(data):
    tag_name_to_tag_node_internal = {}

    def build_tag_node(node_data):
        name = node_data['name']
        children_data = node_data['children']

        children_nodes = []
        for child_data in children_data:
            child_node = build_tag_node(child_data)
            children_nodes.append(child_node)

        node = GNode(name, children_nodes)
        tag_name_to_tag_node_internal[name] = node
        return node

    build_tag_node(data)

    return tag_name_to_tag_node_internal


def get_documents_by_tag(documents, tag, tag_name_to_tag_node):
    if tag not in tag_name_to_tag_node:
        return []
    tag_node = tag_name_to_tag_node[tag]
    sub_nodes = walk_graph(tag_node)
    sub_tags = {node.get_name() for node in sub_nodes}

    return [doc['uri'] for doc in documents if any(t in sub_tags for t in doc['tags'])]
