import clamd


def scan_file(path):
    av_ins = clamd.ClamdUnixSocket()
    results = av_ins.scan(path)
    return results
