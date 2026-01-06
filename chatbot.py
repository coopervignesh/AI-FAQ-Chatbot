from faq_data import faq

def get_response(user_input):
    user_input = user_input.lower().strip()
    return faq.get(user_input, "Sorry, I did not understand that.")
