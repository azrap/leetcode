def segments(message):
    MESSAGE_LIMIT = 160
    MESSAGE_PADDING = 5

    if len(message) <= MESSAGE_LIMIT:
        return message

    messages = []
    message_length = len(message)
    message_limit_calc = MESSAGE_LIMIT - MESSAGE_PADDING
    # not sure if math.ceil allowed
    total_pages = math.ceil((message_length / message_limit_calc)
    for page in range(1, total_pages + 1):
        message_segment=f'{message[:message_limit_calc]}({page}/{total_pages})'
        messages.append(message_segment)
        message=message[message_limit_calc:]

    return messages

    Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus
