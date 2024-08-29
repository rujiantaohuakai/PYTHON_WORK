def show_messages(messages, sent_messages=[]):
    """展示列表里的信息"""
    if messages:
        for message in messages:
            print(message)
    else:
        print(messages)

    for sent_message in sent_messages:
        print(sent_message)


def send_messages(messages, sent_messages):
    """将messages列表里的信息打印并且转移到sent_messages中"""
    messages.reverse() #保持信息原本的顺序
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)
