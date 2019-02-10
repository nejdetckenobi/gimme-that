try:
    import notify2 as Notify
    Notify.init("Gimme That!")
    notification_applicable = True

except Exception:
    notification_applicable = False

DEFAULT_TIMEOUT_FOR_NOTIFICATIONS = 3000


def show_start_notification():
    if notification_applicable:
        n = Notify.Notification(
            'GimmeThat started!',
            'GimmeThat is running now!\n'
        )
        n.set_timeout(DEFAULT_TIMEOUT_FOR_NOTIFICATIONS)
        n.show()


def show_mainpage_opened_notification(username=None):
    if notification_applicable:
        if username:
            n = Notify.Notification(
                'Someone logged in!',
                '"{}" logged in to send you some files'.format(username)
            )
        else:
            n = Notify.Notification(
                'Someone logged in!',
                'Someone logged in to send you some files'
            )
        n.set_timeout(DEFAULT_TIMEOUT_FOR_NOTIFICATIONS)
        n.show()


def show_received_notification(username, files):
    if notification_applicable:
        n = Notify.Notification(
            'Files received!',
            '{} sent you {} files!'.format(username, len(files))
        )
        n.set_timeout(DEFAULT_TIMEOUT_FOR_NOTIFICATIONS)
        n.show()


def show_scanned_and_received_notification(username, files, infected_files):
    if notification_applicable:
        n = Notify.Notification(
            'Files received!',
            (
                '{} sent you {} files!\n'
                '{} of them found infected and removed.'
            ).format(username, len(files), len(infected_files))
        )
        n.set_timeout(DEFAULT_TIMEOUT_FOR_NOTIFICATIONS)
        n.show()
