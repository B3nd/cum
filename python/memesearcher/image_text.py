import mongoengine

class ImageText(mongoengine.Document):
    image_ref = mongoengine.StringField()
    text_without_anything = mongoengine.StringField()
    text_with_low_enhancer = mongoengine.StringField()
    text_with_high_enhancer = mongoengine.StringField()
    gray_text = mongoengine.StringField()
    text_with_CLAHE = mongoengine.StringField()
    only_black_and_white_text = mongoengine.StringField()


    def __str__(self):
        return '***image reference: {}\n*text without anything: \
        \n{}\n*text with low enhance: \n{}\n*text with high enhance: \
        \n{}\n*gray text: \n{}\n*text with CLAHE: \n{}\n*black and white text: \
        \n{}\n'.format(self.image_ref, self.text_without_anything, \
        self.text_with_low_enhancer, self.text_with_high_enhancer, \
        self.gray_text, self.text_with_CLAHE, self.only_black_and_white_text)

    meta = {
        'db_alias' : 'core',
        'collection' : 'images'
    }