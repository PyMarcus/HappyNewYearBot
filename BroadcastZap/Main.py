from Controller.BroadcastZap import BroadcastZap


class Main:
    @staticmethod
    def start():
        # método send msg
        BroadcastZap.send_msg()


if __name__ == '__main__':
    Main.start()
