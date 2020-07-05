def last_video_date(page_token: str):
    last_id_str_list = [str(ord(i)-97) for i in page_token.lower()]
    return int(''.join(last_id_str_list))


def video_date_to_page_token(last_video_id: str):
    page_token_list = [chr(97+int(i)) for i in str(last_video_id)]
    return ''.join(page_token_list).upper()
