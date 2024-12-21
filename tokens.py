from pygments.token import Token

tag_ = {
    "keyword": "blue",
    "keyword_reserved": "blue",
    "string_literal": "green",
    "punc": "black",
    "structure": "orange",
    "func": "orange"
}

token_ = {
    Token.Keyword: "keyword",
    Token.Operator.Word: "keyword",
    Token.Name.Builtin: "structure",
    Token.Punctuation: "punc",
    Token.Literal.Number.Integer: "string_literal",
    Token.Literal.String.Single: "string_literal",
    Token.Literal.String.Double: "string_literal",
    Token.Literal.String: "string_literal",
    Token.Keyword.Reserved: "keyword_reserved",
    Token.Name.Function: "func",
}