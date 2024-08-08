from .prompt_helper import cleanup_message

def build_phi_prompt(conf, query,history,user_name):
    """
    Example prompt:

    <|system|>
    You are a helpful assistant.<|end|>
    <|user|>
    Who are you again?<|end|>
    <|assistant|>
    """

    prompt = "<|system|>\n"
    prompt += conf.SYSTEM_MESSAGE + "\n"

    # Add warmup message to kick off chat into the right direction unless
    # we have a decent amount of chat history
    if hasattr(conf,'WARMUP') and (len(history) <= conf.HISTORY_COUNT):
        prompt += "\n" + conf.WARMUP

    prompt += "Generate " + conf.BOT_NAME + "'s response to the following conversation. Enclose emotes in asterisks. Always stay in character.<|end|>\n"

    if not history == []:
        # build prompt from history + query with
        # optional system message on first instruction
        for msg in history[conf.HISTORY_COUNT * -1:]:
            prompt += "<|user|>\n"
            prompt += cleanup_message(msg[0])
            prompt += "<|end|>\n"
            prompt += "<|assistant|>\n"
            prompt += cleanup_message(msg[1])
            prompt += "<|end|>\n"

    prompt += "<|user|>\n"
    prompt += query
    prompt += "<|end|>\n"
    prompt += "<|assistant|>\n"

    prompt = prompt.replace("###USERNAME###", user_name)

    return prompt
