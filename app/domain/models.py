class text_summery_response:
    summary: str
    input_tok: int
    output_tok: int

    def __init__(self, response):
      self.summary =  response.json()["choices"][0]["message"]["content"]
      self.input_tok = response.json()["usage"]["prompt_tokens"]
      self.output_tok = response.json()["usage"]["completion_tokens"]
