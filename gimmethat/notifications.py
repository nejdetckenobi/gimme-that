try:
    import gi
    gi.require_version('Notify', '0.7')
    from gi.repository import Notify
    Notify.init("Gimme That!")
    #     'login': ,
    #     ,
    #     'virus': ,
    # }
    notification_applicable = True

except Exception:
    notification_applicable = False


def show_start_notification():
    if notification_applicable:
        n = Notify.Notification.new(
            'GimmeThat started!',
            'GimmeThat is running now!\n'
        )
        n.show()


def show_login_notification(username):
    if notification_applicable:
        n = Notify.Notification.new(
            'Someone logged in!',
            '"{}" logged in to send you some files'.format(username)
        )
        n.show()


def show_received_notification(username, files):
    if notification_applicable:
        n = Notify.Notification.new(
            'Files received!',
            '{} sent you {} files!'.format(username, len(files))
        )
        n.show()


def show_scanned_and_received_notification(username, files, infected_files):
    if notification_applicable:
        n = Notify.Notification.new(
            'Files received!',
            (
                '{} sent you {} files!\n'
                '{} of them found infected and removed.'
            ).format(username, len(files), len(infected_files))
        )
        n.show()
