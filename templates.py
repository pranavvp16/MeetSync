template_string = """The text that is delimited in triple backticks/
is a video transcript of developers. It has the start-time and end-time of conversation/
between them, Find all the action items in the transcript with the developer assigned to it/
,start-time and end-time of the action item, and return it in the form of JSON with developer/
as key and the action item as value, start-time key with the start_time value and end-time key/
as end-time value.You can return multiple values of developer who is assigned with multiple tasks
transcript = ```{transcript}```
"""