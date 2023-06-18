import json


def get_all_conversation(file_name : str) -> list:
    '''
    get the conversation from the text file

    Args:
        file_name : the name of the text file
    
    Return:
        a list containing the conversation
    
    Note:
        each line of the text file should be in the following format:
        {"id": "dialogue-00000",
        "conversation": 
            [
                {"role": "speaker1", "utterance": "你的朋友会找你讨论感情问题吗，我现在一个头两个大", "response_candidates": ["不会，我都是直接把我的感情经历讲给他们听", "会，而且都是找我诉苦",...]},
                {"role": "speaker2", "utterance": "会啊，然后我就把我的故事都和她讲一遍，她就又自己纠结去了", "response_candidates":[...]},
                ...
            ]
        }
    '''
    conversations = []

    with open(file_name, "r",encoding='utf-8') as f:
        for line in f:
            conversation = json.loads(line)
            conversations.append(conversation)

    return conversations

def get_all_utterances(conversations : list) -> list:
    '''
    get all the utterances from the conversation

    Args:
        conversations : a list containing the conversation

    Return:
        a list containing all the utterances
    '''
    utterances = []
    for conversation in conversations:
        for utterance in conversation["conversation"]:
            utterances.append(utterance["utterance"])
    return utterances



if __name__ == "__main__":
    conversations = get_all_conversation("test.txt")
    utterances = get_all_utterances(conversations)
    print(utterances)
    print(conversations)


