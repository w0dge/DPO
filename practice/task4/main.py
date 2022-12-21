from git import Repo as gItm
import reposInfo as rI


def read_repo_names(path):
    with open(path) as f:
        names = [line.rstrip() for line in f]
        names = list(set(names))
        return names


def clone_repo(name_set, path_to_save, git_url):
    report = []
    for i in range(len(name_set)):
        try:
            gItm.clone_from(url=git_url + name_set[i], to_path=path_to_save + name_set[i])
        except Exception as ex:
            print(f"Exception: {type(ex).__name__}. Arguments:\n{ex.args!r}")
            report.append((name_set[i], "FAIL"))
            continue
        report.append((name_set[i], "OK"))
    return report


def save_report_to_file(save_path, report):
    with open(save_path, "w") as f:
        f.write("Report\n")
        for record in report:
            f.write(f"{record[0]} (status: {record[1]})\n")


if __name__ == "__main__":
    repo_names = read_repo_names(rI.repos_names_path)
    print("Repositories names are set from file:")
    for num in range(len(repo_names)):
        print(f"Repo №{num + 1}: {repo_names[num]}")

    report = clone_repo(repo_names, rI.repo_clone_path, rI.base_url)
    save_report_to_file(rI.report_save_path, report)
