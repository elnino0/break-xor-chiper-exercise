from main.decrypt_xor_exc import guess_key, xor_decrypt, xor_strings

from unittest import TestCase


class guessXorKeyTesting(TestCase):

    def test_selfKey(self):
        text = "axbcdefg"
        key = "axbcdefg"
        encrypted_text = xor_strings(text.encode(), key.encode())
        self.assertEqual(encrypted_text, b'\x00\x00\x00\x00\x00\x00\x00\x00',
                         msg="encrypted_text should be zero with self key")

        text_result = xor_decrypt(encrypted_text, key.encode())
        self.assertEqual(text, text_result, msg="origin text not equal to his decrypt")

    def test_encryptDecrypt(self):
        text = "axbcdefg"
        key = "abc"
        encrypted_text = xor_strings(text.encode(), key.encode())
        text_result = xor_decrypt(encrypted_text, key.encode())
        self.assertEqual(text, text_result, msg="origin text not equal to his decrypt")

    def test_happyFlow_guessTheKey(self):
        text = "axbc312defg()"
        key = "abc"
        encrypted_text = xor_strings(text.encode(), key.encode())
        possible_match = guess_key(encrypted_text.decode("ascii"), len(key))
        self.assertTrue((text, key) in possible_match, msg="expected key and text found in possible key text list")

    def test_noKey_guessTheKey(self):
        text = "axbcdefg"
        possible_match = guess_key(text, 3)

        for item in possible_match:
            self.assertFalse(text in item, msg="text should not found in possible match list with no key is used ")



    def test_numberlist_guessTheKey(self):
        text = "ax()b...cdefg31 2JKJ KKJH312 '\n' halloooo"
        key = "abc"

        encrypted_text = xor_strings(text.encode(), key.encode())
        encrypted_text_as_number_list = list(encrypted_text)
        possible_match = guess_key(encrypted_text_as_number_list, len(key))

        self.assertTrue((text, key) in possible_match, msg="expected key and text found in possible key text list")

    def test_worngLen_guessTheKey(self):
        text = "axbcdefg"
        key = "abc"
        encrypted_text = xor_strings(text.encode(), key.encode())
        possible_match = guess_key(encrypted_text.decode("ascii"), len(key) - 1)

        for item in possible_match:
            self.assertFalse(text in item, msg="text should not found in possible match list with no key is used ")

    def test_BadLetter_guessTheKey(self):
        text = "axbcdefg¥"
        key = "abc"
        encrypted_text = xor_strings(text.encode(), key.encode())
        with self.assertRaises(UnicodeDecodeError):
            guess_key(encrypted_text.decode(), len(key))


