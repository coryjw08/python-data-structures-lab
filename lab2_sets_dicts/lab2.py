# =============================================================
#  LAB 2: Sets and Dictionaries (about 25 minutes)
# =============================================================
#
#  A SET holds unique items with no order. Duplicates disappear.
#  Checking "is X in this set?" is fast: O(1).
#      s = {"10.0.0.5", "10.0.0.8"}
#
#  A DICTIONARY (dict) maps a KEY to a VALUE, like a lookup table.
#  Looking up a key is also fast: O(1).
#      services = {22: "ssh", 80: "http"}
#      services[22]   ->  "ssh"
#
#  How to work:
#    1. Read each TODO comment.
#    2. Replace the None with your answer.
#    3. Run this file:  python lab2_sets_dicts/lab2.py
#    4. The checker at the bottom shows PASS or FAIL for each task.
# =============================================================


# ----- Starting data (do not change these lines) -----

# IPs pulled from a firewall log. Some show up more than once.
ips = ["10.0.0.5", "203.0.113.9", "10.0.0.5", "10.0.0.8", "203.0.113.9", "10.0.0.12"]

# IPs we SAW talking on the network today.
seen = ["10.0.0.5", "10.0.0.8", "10.0.0.12", "198.51.100.23"]

# IPs in our official asset INVENTORY (machines we know we own).
inventory = ["10.0.0.5", "10.0.0.8", "10.0.0.12", "10.0.0.20"]

# Port number -> service name.
services = {22: "ssh", 80: "http", 443: "https"}


# ===== Part A: Sets =====

# TODO 1: Remove the duplicates from ips by turning the list into a set.
#         Use the set() function.
#         Expected: {"10.0.0.5", "203.0.113.9", "10.0.0.8", "10.0.0.12"}
#         (Sets have no order, so yours may print in a different order. That is fine.)
unique_ips = None


# TODO 2: How many UNIQUE IPs are there? Use len() on your set.
#         Expected: 4
unique_count = None


# TODO 3: Is "203.0.113.9" in unique_ips? Use the "in" keyword.
#         "in" gives back True or False.
#         Expected: True
is_listed = None


# TODO 4: Which IPs are in BOTH seen and inventory?
#         Turn each list into a set, then use & (AND) between them.
#         & keeps only the items that are in both sets.
#         Expected: {"10.0.0.5", "10.0.0.8", "10.0.0.12"}
in_both = None


# TODO 5: Which IPs did we SEE that are NOT in our inventory?
#         Turn each list into a set, then use - (minus).
#         A - B keeps the items in A that are not in B. Order matters!
#         Expected: {"198.51.100.23"}
#
#         Real world: this is how you spot an UNMANAGED DEVICE. Something is
#         talking on our network, but it is not on our list of known machines.
#         That deserves a closer look.
unknown_hosts = None


# ===== Part B: Dictionaries =====

# TODO 6: Look up the service name for port 22 in services.
#         Use square brackets with the key: services[...]
#         Expected: "ssh"
ssh_name = None


# TODO 7: Add port 3389 with the name "rdp" to services.
#         This task is an action, not a variable. Write your line on the
#         empty line just below this comment. Pattern:  my_dict[key] = value
#         Hint: the key is the NUMBER 3389, not the text "3389".
#         Expected: services[3389] gives back "rdp"


# TODO 8: Look up port 8080. It is NOT in services, so services[8080]
#         would crash with a KeyError. Use the .get() method instead,
#         and make it give back "unknown" when the port is missing.
#         .get() takes a second value to use when the key is not found.
#         Expected: "unknown"
port_8080 = None


# ----- Show your results -----
print("Your results:")
print("  unique_ips    =", unique_ips)
print("  unique_count  =", unique_count)
print("  is_listed     =", is_listed)
print("  in_both       =", in_both)
print("  unknown_hosts =", unknown_hosts)
print("  ssh_name      =", ssh_name)
print("  services      =", services)
print("  port_8080     =", port_8080)
print()


# =============================================================
#  CHECKER: DO NOT EDIT BELOW THIS LINE
#  Run this file to check your work: python lab2.py
# =============================================================
#
#  Curious how the checker works? Read on. Each check_task_...
#  function looks at one of your variables and prints PASS or FAIL.
#  "try" / "except" catches errors so one broken task cannot stop
#  the other checks from running.

LAB_NUMBER = 2


def report(number, name, passed, hint=""):
    """Print one PASS/FAIL line and return True or False."""
    if passed:
        print(f"PASS  Task {number}: {name}")
    else:
        print(f"FAIL  Task {number}: {name} ({hint})")
    return passed


def check_set_task(number, name, value, expected, how_hint):
    """Shared logic for Tasks 1, 4, and 5: the answer must be a real set."""
    if value is None:
        return report(number, name, False, f"got None. {how_hint}")
    if type(value) is set and value == expected:
        return report(number, name, True)
    if type(value) in (list, tuple, frozenset, dict) and set(value) == expected:
        # Right items, wrong data structure. The lecture cares about this.
        return report(number, name, False,
                      f"the right IPs, but it is a {type(value).__name__}, not a set. {how_hint}")
    # Show the expected set with { } so it does not look like a list.
    shown = "{" + ", ".join(repr(item) for item in sorted(expected)) + "}"
    return report(number, name, False, f"expected {shown}, got {value!r}. {how_hint}")


def check_task_1_unique_ips():
    try:
        expected = {"10.0.0.5", "203.0.113.9", "10.0.0.8", "10.0.0.12"}
        return check_set_task(1, "unique_ips", unique_ips, expected,
                              "Did you use set() on ips?")
    except Exception as error:
        return report(1, "unique_ips", False, f"checker error: {error}")


def check_task_2_unique_count():
    try:
        if unique_count == 4 and type(unique_count) is int:
            return report(2, "unique_count", True)
        if unique_count is None:
            return report(2, "unique_count", False, "expected 4, got None. Did you use len()?")
        if unique_count == 6:
            return report(2, "unique_count", False,
                          "got 6. That counts the original list with duplicates. "
                          "Use len() on unique_ips instead")
        return report(2, "unique_count", False,
                      f"expected 4, got {unique_count!r}. Did you use len() on unique_ips?")
    except Exception as error:
        return report(2, "unique_count", False, f"checker error: {error}")


def check_task_3_is_listed():
    try:
        if is_listed is True:
            return report(3, "is_listed", True)
        if is_listed is None:
            return report(3, "is_listed", False,
                          "expected True, got None. Use the 'in' keyword: something in unique_ips")
        if is_listed == "True":
            return report(3, "is_listed", False,
                          "got the text 'True'. Let 'in' give you a real True/False, no quotes")
        if is_listed is False:
            return report(3, "is_listed", False,
                          "got False. Check the IP is typed exactly right, and that you searched unique_ips")
        return report(3, "is_listed", False,
                      f"expected True, got {is_listed!r}. The 'in' keyword gives back True or False")
    except Exception as error:
        return report(3, "is_listed", False, f"checker error: {error}")


def check_task_4_in_both():
    try:
        expected = {"10.0.0.5", "10.0.0.8", "10.0.0.12"}
        return check_set_task(4, "in_both", in_both, expected,
                              "Turn seen and inventory into sets, then use &")
    except Exception as error:
        return report(4, "in_both", False, f"checker error: {error}")


def check_task_5_unknown_hosts():
    try:
        expected = {"198.51.100.23"}
        if unknown_hosts == {"10.0.0.20"}:
            return report(5, "unknown_hosts", False,
                          "got {'10.0.0.20'}. That is backwards: it is in inventory but not seen. "
                          "With minus, order matters. Put seen first")
        return check_set_task(5, "unknown_hosts", unknown_hosts, expected,
                              "Turn seen and inventory into sets, then use -")
    except Exception as error:
        return report(5, "unknown_hosts", False, f"checker error: {error}")


def check_task_6_ssh_name():
    try:
        if ssh_name == "ssh":
            return report(6, "ssh_name", True)
        if ssh_name is None:
            return report(6, "ssh_name", False,
                          "expected 'ssh', got None. Look up a key with square brackets: services[...]")
        return report(6, "ssh_name", False,
                      f"expected 'ssh', got {ssh_name!r}. The key is the port number 22")
    except Exception as error:
        return report(6, "ssh_name", False, f"checker error: {error}")


def check_task_7_add_rdp():
    try:
        if (services.get(3389) == "rdp" and services.get(22) == "ssh"
                and services.get(80) == "http" and services.get(443) == "https"):
            return report(7, "add rdp to services", True)
        if services.get(3389) == "rdp":
            # Usually: services = {3389: "rdp"}, which throws away the old ports.
            return report(7, "add rdp to services", False,
                          "3389 is there, but ports 22, 80, or 443 are gone. Add ONE key to the "
                          "existing dictionary with my_dict[key] = value. Don't make a new one")
        if "3389" in services:
            return report(7, "add rdp to services", False,
                          "you used the text '3389' as the key. The other keys are numbers, so use 3389 with no quotes")
        if 3389 in services:
            return report(7, "add rdp to services", False,
                          f"port 3389 is there, but its name is {services[3389]!r}, not 'rdp'")
        return report(7, "add rdp to services", False,
                      "port 3389 is not in services yet. Pattern: my_dict[key] = value")
    except Exception as error:
        return report(7, "add rdp to services", False, f"checker error: {error}")


def check_task_8_port_8080():
    try:
        if port_8080 == "unknown":
            return report(8, "port_8080", True)
        if port_8080 is None:
            return report(8, "port_8080", False,
                          "expected 'unknown', got None. If you used .get(), give it a "
                          "second value to use when the port is missing")
        return report(8, "port_8080", False,
                      f"expected 'unknown', got {port_8080!r}. Use .get() on services")
    except Exception as error:
        return report(8, "port_8080", False, f"checker error: {error}")


def run_checks():
    print("=" * 50)
    print(f"Checking Lab {LAB_NUMBER}...")
    print("=" * 50)
    results = [
        check_task_1_unique_ips(),
        check_task_2_unique_count(),
        check_task_3_is_listed(),
        check_task_4_in_both(),
        check_task_5_unknown_hosts(),
        check_task_6_ssh_name(),
        check_task_7_add_rdp(),
        check_task_8_port_8080(),
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
