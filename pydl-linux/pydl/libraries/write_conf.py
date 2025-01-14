from libraries import get_app_path


def main(conf):
    to_write = []
    to_write.append("[Flags]\n")
    to_write.append(f'playlist = {conf["playlist"]}\n')
    to_write.append(f'tag = {conf["tag"]}\n')
    to_write.append(f'experimental = {conf["experimental"]}\n')
    to_write.append(f'manual-tag = {conf["manual-tag"]}\n')
    to_write.append(f'tn-as-cover = {conf["tn_as_cover"]}\n')
    to_write.append(f'upload = {conf["upload"]}\n')
    to_write.append(f'complex-filetree = {conf["complex-filetree"]}\n')
    to_write.append(f'skip-existing = {conf["skip-existing"]}\n')
    to_write.append("\n")
    to_write.append("[General]\n")
    to_write.append(f'dl-limit = {conf["dl-limit"]}\n')

    # full path to the config file. works because the config file is in the same directory as the running file
    full_path = get_app_path.config()

    # open the config file and prepare for translation
    conf_file = open(full_path, "w")

    conf_file.writelines(to_write)
    conf_file.close()
