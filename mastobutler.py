"""
Mastobutler, bot for wellcome new users in a Mastodon instance
"""

from pybot.mastobot import Mastobot

BOT_NAME = "Butlerbot"
MAX_LENGHT = 490

class Bot(Mastobot):
    """ Main class of a Mastodon bot """

    def __init__(self, botname: str = BOT_NAME) -> None:

        super().__init__(botname = botname)

        self.init_publish_bot()
        self.init_replay_bot()


    def run(self, botname: str = BOT_NAME) -> None:

        posts = []

        notifications = self.get_notifications()
        for notif in notifications:

            content = self.check_notif(notif, "admin.sign_up")
            if content != "":

                for text_post in self._actions.get("wellcome.posts"):
                    posts.append(self.find_text(notif, text_post))

                self.post_toot (posts, "es")

        super().run(botname = botname)


    def find_text(self, notif, text_post):
        """ find the text to post """

        username = notif.account.acct

        post_text  = "@" + username + " " + text_post + "\n\n" + self._actions.get("wellcome.hashtag")
        post_text  = (post_text[:MAX_LENGHT] + '... ') if len(post_text) > MAX_LENGHT else post_text

        self._logger.debug ("answering text\n%s", post_text)

        return post_text


# main

if __name__ == '__main__':
    Bot().run()
