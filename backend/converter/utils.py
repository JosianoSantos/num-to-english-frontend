def number_to_words(n):
    def convert_chunk(num):
        below_20 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
                    'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
                    'nineteen']
        tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
        if num < 20:
            return below_20[num]
        elif num < 100:
            return tens[num // 10] + (' ' + below_20[num % 10] if num % 10 else '')
        else:
            return below_20[num // 100] + ' hundred' + (' ' + convert_chunk(num % 100) if num % 100 else '')

    if n == 0:
        return "zero"

    big_units = ['', 'thousand', 'million', 'billion', 'trillion']
    words = []
    chunk_count = 0

    while n:
        chunk = n % 1000
        if chunk:
            words.append((convert_chunk(chunk) + ' ' + big_units[chunk_count]).strip())
        n //= 1000
        chunk_count += 1

    return ' '.join(reversed(words))