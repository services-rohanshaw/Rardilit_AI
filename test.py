from opengpt.models.completion.usesless.model import Model
usesless=Model()
message_id = ""
while True:
    prompt = input("Question: ")
    if prompt == "!stop":
        break

    # req = usesless.Completion.create(prompt=prompt, parentMessageId=message_id)

    # print(f"Answer: {req['text']}")
    # message_id = req["id"]
    usesless.SetupConversation(prompt)
    response = ''
    for r in usesless.SendConversation():
        response += r.choices[0].delta.content
    if not response:
        response = "I couldn't generate a response. Please try again."
    print(response) 