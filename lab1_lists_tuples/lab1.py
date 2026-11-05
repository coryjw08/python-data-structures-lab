# =============================================================
#  LAB 1: Lists and Tuples (warm-up, about 20 minutes)
# =============================================================
#
#  A LIST holds items in order, and you can change it.
#      hosts = ["web01", "db01"]
#
#  A TUPLE also holds items in order, but you CANNOT change it.
#      record = ("10.0.0.5", 22, "tcp")
#
#  How to work:
#    1. Read each TODO comment.
#    2. Replace the None with your answer.
#    3. Run this file:  python lab1_lists_tuples/lab1.py
#    4. The checker at the bottom shows PASS or FAIL for each task.
#
#  Do the tasks in order. Later tasks depend on earlier ones.
# =============================================================


# ----- Starting data (do not change these two lines) -----
hosts = ["web01", "db01", "mail01", "dns01"]
record = ("10.0.0.5", 22, "tcp")


# TODO 1: A new web server came online. Add "web02" to the END of hosts.
#         Use the .append() method. This task is an action, not a variable:
#         write your line on the empty line just below this comment.
#         Expected: hosts becomes ["web01", "db01", "mail01", "dns01", "web02"]



# TODO 2: Get the FIRST host in the list using an index.
#         Remember: Python starts counting at 0.
#         Expected: "web01"
first_host = None


# TODO 3: Get the LAST host in the list using a NEGATIVE index.
#         Negative indexes count from the end of the list.
#         Expected: "web02"   (because you added it in Task 1)
last_host = None


# TODO 4: Count how many hosts are in the list. Use the len() function.
#         Expected: 5
host_count = None


# TODO 5: Make a NEW list with the hosts in alphabetical order.
#         Use the sorted() FUNCTION, not the .sort() METHOD.
#           sorted(x)  gives you back a new sorted list. x stays the same.
#           x.sort()   sorts x itself and gives you back None.
#         Expected: ["db01", "dns01", "mail01", "web01", "web02"]
#         And hosts must stay in its original order.
sorted_hosts = None


# TODO 6: Unpack the tuple "record" into three variables in ONE line.
#         Replace "None, None, None" with the name of the tuple.
#         Python puts the first item in ip, the second in port,
#         and the third in protocol.
#         Expected: ip = "10.0.0.5", port = 22, protocol = "tcp"
ip, port, protocol = None, None, None


# ----- Show your results -----
print("Your results:")
print("  hosts        =", hosts)
print("  first_host   =", first_host)
print("  last_host    =", last_host)
print("  host_count   =", host_count)
print("  sorted_hosts =", sorted_hosts)
print("  ip, port, protocol =", ip, port, protocol)
print()


# =============================================================
#  CHECKER: DO NOT EDIT BELOW THIS LINE
#  Run this file to check your work: python lab1.py
# =============================================================
#
#  Curious how the checker works? Read on. Each check_task_...
#  function looks at one of your variables and prints PASS or FAIL.
#  "try" / "except" catches errors so one broken task cannot stop
#  the other checks from running.

LAB_NUMBER = 1
ORIGINAL_ORDER = ["web01", "db01", "mail01", "dns01", "web02"]


def report(number, name, passed, hint=""):
    """Print one PASS/FAIL line and return True or False."""
    if passed:
        print(f"PASS  Task {number}: {name}")
    else:
        print(f"FAIL  Task {number}: {name} ({hint})")
    return passed


def check_task_1_append():
    try:
        if hosts == ORIGINAL_ORDER:
            return report(1, "append web02", True)
        if hosts is None:
            # The classic mistake: hosts = hosts.append(...) or hosts = hosts.sort()
            return report(1, "append web02", False,
                          "hosts is None. .append() and .sort() change the list and give back None, "
                          "so write hosts.append(...) on its own, not hosts = hosts.append(...)")
        if len(hosts) == 4:
            return report(1, "append web02", False,
                          "hosts still has 4 items. Use hosts.append(...) to add one to the end")
        if len(hosts) == 5 and hosts[-1] == "web02":
            # Right item at the end, but the order changed. Usually .sort() in Task 5.
            return report(1, "append web02", False,
                          "web02 is there, but hosts is no longer in its original order. "
                          "Did you use .sort() in Task 5? That changes hosts itself")
        if "web02" in hosts and hosts[-1] != "web02":
            return report(1, "append web02", False,
                          "web02 must go at the END. .append() always adds to the end")
        return report(1, "append web02", False,
                      f"expected 5 hosts ending in 'web02', got {hosts!r}. "
                      "Did you run .append() more than once?")
    except Exception as error:
        return report(1, "append web02", False, f"checker error: {error}")


def check_task_2_first_host():
    try:
        if first_host == "web01":
            return report(2, "first_host", True)
        if first_host is None:
            return report(2, "first_host", False,
                          "expected 'web01', got None. Use an index in square brackets: hosts[...]")
        if first_host == "db01":
            return report(2, "first_host", False,
                          "got 'db01'. Remember: Python starts counting at 0, not 1")
        return report(2, "first_host", False,
                      f"expected 'web01', got {first_host!r}. The first item is at index 0")
    except Exception as error:
        return report(2, "first_host", False, f"checker error: {error}")


def check_task_3_last_host():
    try:
        if last_host == "web02":
            return report(3, "last_host", True)
        if last_host is None:
            return report(3, "last_host", False,
                          "expected 'web02', got None. Remember: negative indexes count from the end")
        if last_host == "dns01":
            return report(3, "last_host", False,
                          "got 'dns01'. Did you finish Task 1 first? web02 should be last now")
        return report(3, "last_host", False,
                      f"expected 'web02', got {last_host!r}. "
                      "Remember: negative indexes count from the end")
    except Exception as error:
        return report(3, "last_host", False, f"checker error: {error}")


def check_task_4_host_count():
    try:
        if host_count == 5 and type(host_count) is int:
            return report(4, "host_count", True)
        if host_count is None:
            return report(4, "host_count", False, "expected 5, got None. Did you use len()?")
        if host_count == 4:
            return report(4, "host_count", False,
                          "got 4. Did you finish Task 1 first? There should be 5 hosts now")
        if host_count == "5":
            return report(4, "host_count", False,
                          "got the text '5', not the number 5. Use len(), and no quotes")
        return report(4, "host_count", False,
                      f"expected 5, got {host_count!r}. Did you use len()?")
    except Exception as error:
        return report(4, "host_count", False, f"checker error: {error}")


def check_task_5_sorted_hosts():
    try:
        expected = ["db01", "dns01", "mail01", "web01", "web02"]
        if sorted_hosts is None and hosts == expected:
            # The classic mistake: sorted_hosts = hosts.sort()
            return report(5, "sorted_hosts", False,
                          "got None, and hosts itself got sorted. That is what .sort() does: "
                          "it changes the list and gives back None. Use the sorted() function")
        if sorted_hosts is None:
            return report(5, "sorted_hosts", False,
                          "expected a sorted list, got None. Did you use sorted()?")
        if sorted_hosts == expected and hosts == expected:
            return report(5, "sorted_hosts", False,
                          "sorted_hosts is right, but hosts got sorted too. "
                          "Use sorted(hosts) so the original list stays the same")
        if sorted_hosts == expected:
            # hosts itself is not sorted, so sorted() did its job.
            # (If hosts is wrong for another reason, Task 1 reports it.)
            return report(5, "sorted_hosts", True)
        if sorted_hosts == ["db01", "dns01", "mail01", "web01"]:
            return report(5, "sorted_hosts", False,
                          "web02 is missing. Did you finish Task 1 first?")
        return report(5, "sorted_hosts", False,
                      f"expected {expected!r}, got {sorted_hosts!r}. Did you use sorted()?")
    except Exception as error:
        return report(5, "sorted_hosts", False, f"checker error: {error}")


def check_task_6_unpack():
    try:
        if (ip, port, protocol) == ("10.0.0.5", 22, "tcp"):
            return report(6, "ip, port, protocol", True)
        if ip is None and port is None and protocol is None:
            return report(6, "ip, port, protocol", False,
                          "all three are still None. Replace 'None, None, None' with the tuple's name")
        if port == "22":
            return report(6, "ip, port, protocol", False,
                          "port is the text '22', but in record it is the number 22")
        return report(6, "ip, port, protocol", False,
                      f"expected '10.0.0.5', 22, 'tcp', got {ip!r}, {port!r}, {protocol!r}. "
                      "The names on the left line up with the items in the tuple, in order")
    except Exception as error:
        return report(6, "ip, port, protocol", False, f"checker error: {error}")


def run_checks():
    print("=" * 50)
    print(f"Checking Lab {LAB_NUMBER}...")
    print("=" * 50)
    results = [
        check_task_1_append(),
        check_task_2_first_host(),
        check_task_3_last_host(),
        check_task_4_host_count(),
        check_task_5_sorted_hosts(),
        check_task_6_unpack(),
    ]
    passed = results.count(True)
    print("-" * 50)
    print(f"{passed}/{len(results)} tasks passing")
    if passed == len(results):
        print()
        print(f"Lab {LAB_NUMBER} complete: commit and push your work.")
        print("    git add .")
        print(f'    git commit -m "Finished lab {LAB_NUMBER}"')
        print("    git push")
    else:
        print("Read the FAIL hints above, fix those tasks, and run this file again.")


run_checks()
