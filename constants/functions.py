def generate_uid(uid_tag):
    """
    :param uid_tag: must be 3 digit
    :return: uid_tag + firsthalfTimeStamp + generateString + secondHalfTimeStamp as string
    """

    ts = str(time.time())
    first_half_ts = ts[0:ts.find('.')].zfill(10)
    second_half_ts = ts[ts.find('.') + 1:].zfill(10)

    generated_string = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))

    generated_uid = f"{uid_tag}-{first_half_ts}-{generated_string}-{second_half_ts}"

    return generated_uid