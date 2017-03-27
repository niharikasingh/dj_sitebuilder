import json
import os


def make_cardlist(path2model):

    # Create array cardlist for storing cards
    cardlist = []

    with open(path2model, 'r') as question_text_file:
        question_data = question_text_file.read()
        question_json = json.loads(question_data)

    # Store two arrays in question_json in node_data_array and link_data_array
    node_data_array = question_json['nodeDataArray']
    link_data_array = question_json['linkDataArray']

    print node_data_array
    print link_data_array

    found_question_keys = find_question_keys(node_data_array, link_data_array)

    for question_key in found_question_keys[0]:
        question = make_buttons(question_key, node_data_array, link_data_array)
        print 'question coming up!'
        print question
        cardlist.append(question)

    # Return cardlist
    return cardlist


def find_question_keys(node_data_array, link_data_array):

    # Initialize array question_keys, as an array of arrays question_key_array and button_key_array
    question_key_array = []
    button_key_array = []
    question_keys = [question_key_array, button_key_array]

    # Iterate over each node in node_data_array, appending it to question_key_array if it is a question
    for node in node_data_array:
        try:
            if node['card_type'] == 'textbox' or 'select':
                    question_key_array.append(node['key'])
            else:
                    button_key_array.append(node['key'])
        except:
            pass

    return question_keys


def make_buttons(question_key, node_data_array, link_data_array):

    # Initilaize dict to store button_list
    button_list = {}

    # Iterate over links in link_data_array
    for link in link_data_array:

        # If a link's from is the same as the question_key, do the following
        if link['from'] == question_key:

            found_button_key = link['to']
            found_button_direction = find_button_direction(found_button_key, node_data_array, link_data_array)
            found_button_text = find_button_text(found_button_key, node_data_array, link_data_array)
            found_direction_id = find_direction_id(found_button_direction, node_data_array, link_data_array)

            button_list.update({found_button_text: found_direction_id})

    # Iterate over nodes in node_data_array, adding buttons to each card before returning the node
    for node in node_data_array:
        if node['key'] == question_key:
            node.update({'card_buttons': button_list})
            return node

def find_button_direction(found_button_key, node_data_array, link_data_array):
    for link in link_data_array:
        if link['from'] == found_button_key:
            return link['to']

def find_button_text(found_button_key, node_data_array, link_data_array):
    for node in node_data_array:
        try:
            if node['key'] == found_button_key:
                return node['card_text']
        except:
            pass

def find_direction_id(found_button_direction, node_data_array, link_data_array):
    for node in node_data_array:
        try:
            if node['key'] == found_button_direction:
                return node['card_id']
        except:
            pass