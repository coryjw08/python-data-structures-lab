# =============================================================
#  LAB 4: Capstone. Brute-Force Login Detector (about 40 minutes)
# =============================================================
#
#  The story: data/auth.log is an SSH log from a Linux server. Someone is
#  guessing passwords. Find out who, using the four data structures:
#
#    LIST        the raw log lines, in the order they happened
#    SET         the allowlist and the threat-intel feed (fast "is it in here?")
#    DICTIONARY  counting failed logins per IP (IP -> count)
#    TUPLE       each alert record: (ip, count), a fixed pair that won't change
#
#  This is the real-world pattern from the lecture: data arrives as a
#  list, and you turn it into sets and dicts for fast lookups.
#
#  A failed login line looks like one of these:
#    Nov  5 10:01:02 web01 sshd[1201]: Failed password for root from 203.0.113.9 port 51515 ssh2
#    Nov  5 10:01:10 web01 sshd[1203]: Failed password for invalid user admin from 198.51.100.23 port 50001 ssh2
#
#  How to work:
#    1. Read each TODO comment and replace the None with your answer.
#    2. Run this file:  python lab4_capstone/lab4.py
#    3. The checker at the bottom shows PASS or FAIL for each task.
#
#  Do the tasks in order. Each one uses the one before it.
# =============================================================

# This line loads a tool that comes with Python. "Path" helps us find files.
from pathlib import Path

# ----- Starting data (do not change these lines) -----

# Find the data folder next to this lab, no matter where you run it from.
DATA_FOLDER = Path(__file__).parent.parent / "data"
LOG_FILE = DATA_FOLDER / "auth.log"
BAD_IPS_FILE = DATA_FOLDER / "bad_ips.txt"

THRESHOLD = 10              # alert when an IP has MORE than this many failures
allowlist = {"10.0.0.5"}    # trusted internal vulnerability scanner. Never alert on it.


# ===== Step 1: Read the log (LIST) =====

# TODO 1: Read the log file into a list of strings, one string per line.
#         Use exactly this pattern:   open(LOG_FILE).read().splitlines()
#           .read()        gives you the whole file as one big string
#           .splitlines()  cuts that string into a list, one item per line
#         Expected: a list of 401 strings
lines = None


# ===== Step 2: Count failed logins per IP (DICTIONARY) =====
#
# fails will map each IP to how many times it failed to log in.
# For example: {"203.0.113.9": 47, "10.0.0.8": 2, ...}

fails = {}

# "lines or []" just keeps this loop from crashing before Task 1 is done.
for line in lines or []:

    # We only care about failed logins. Skip every other line.
    if "Failed password" in line:

        # TODO 2a: Get the IP address out of this line.
        #          line.split() cuts the line into words at the spaces.
        #          In both kinds of "Failed password" lines, the IP is the
        #          4th word from the END. Use a negative index: line.split()[-4]
        #          Expected (for the first failed line): "198.51.100.150"
        ip = None

        # TODO 2b: Work out this IP's new count: its old count plus one.
        #          The first time we see an IP, it is not in fails yet, so
        #          fails[ip] would crash. Use .get() with a default of 0:
        #              fails.get(ip, 0) + 1
        new_count = None

        # Save the new count in the dictionary (already done for you).
        fails[ip] = new_count

# Expected after Step 2: 12 different IPs, 161 failed logins in total.


# ===== Step 3: Find the attackers (TUPLES in a LIST) =====

alerts = []         # list of (ip, count) tuples
alert_ips = set()   # just the IPs, as a set (used in Step 5)

for ip in fails:
    # "or 0" just keeps this loop from crashing before Task 2b is done.
    count = fails[ip] or 0

    # TODO 3: Set is_alert to True or False. An IP is an alert when BOTH:
    #           - count is MORE than THRESHOLD  (use >, not >=)
    #           - ip is NOT in allowlist        (use "not in")
    #         Join the two tests with the word "and".
    #         Expected: 4 alerts in total
    is_alert = None

    if is_alert:
        # Each alert is a TUPLE (ip, count). Already done for you.
        alerts.append((ip, count))
        alert_ips.add(ip)


# ===== Step 4: Load the threat-intel feed (SET) =====

# TODO 4: Read bad_ips.txt into a SET of strings, one IP per line.
#         Same pattern as Task 1, but wrap it in set( ... ).
#         Use the BAD_IPS_FILE variable for the file name.
#         Expected: a set of 25 IPs
threat_intel = None


# ===== Step 5: Confirm with threat intel (SET &) =====

# TODO 5: Which of our alert IPs are ALSO in threat_intel?
#         Use & between the two sets: alert_ips and threat_intel.
#         Expected: a set of 2 IPs
confirmed = None


# ===== Step 6: Print the report (already done for you) =====

print("=" * 50)
print("BRUTE-FORCE LOGIN REPORT")
print("=" * 50)
if lines is not None:
    print(f"Log lines read:       {len(lines)}")
print(f"IPs with failures:    {len(fails)}")
print(f"Alert threshold:      more than {THRESHOLD} failures")
print(f"Allowlisted:          {allowlist}")
print()
if len(alerts) == 0:
    print("No alerts yet. Finish Tasks 1 to 3 to see them here.")
for ip, count in alerts:
    note = ""
    if confirmed is not None and ip in confirmed:
        note = "   <-- CONFIRMED by threat intel"
    print(f"  ALERT  {ip:<16} {count:>3} failed logins{note}")
print()


# =============================================================
#  CHECKER: DO NOT EDIT BELOW THIS LINE
#  Run this file to check your work: python lab4.py
# =============================================================
#
#  Curious how the checker works? Read on. The checker works out the right
#  answers on its own, straight from the data files, using a DIFFERENT
#  method than you did (it counts with a separate loop). Then it compares
#  its answers with yours. "try" / "except" catches errors so one broken
#  task cannot stop the other checks from running.

LAB_NUMBER = 4


def report(number, name, passed, hint=""):
    """Print one PASS/FAIL line and return True or False."""
    if passed:
        print(f"PASS  Task {number}: {name}")
    else:
        print(f"FAIL  Task {number}: {name} ({hint})")
    return passed


def expected_lines():
    return LOG_FILE.read_text().splitlines()


def expected_fails():
    """Count failed logins per IP by finding the word after 'from'."""
    counts = {}
    for log_line in expected_lines():
        if "Failed password" not in log_line:
            continue
        words = log_line.split()
        address = words[words.index("from") + 1]
        if address in counts:
            counts[address] = counts[address] + 1
        else:
            counts[address] = 1
    return counts


def expected_alerts():
    result = []
    for address, total in expected_fails().items():
        if total > THRESHOLD and address not in allowlist:
            result.append((address, total))
    return result


def expected_threat_intel():
    result = set()
    for raw in open(BAD_IPS_FILE):
        if raw.strip() != "":
            result.add(raw.strip())
    return result


def check_task_1_lines():
    try:
        expected = expected_lines()
        if type(lines) is list and lines == expected:
            return report(1, "lines", True)
        if lines is None:
            return report(1, "lines", False,
                          "got None. Use the pattern in the TODO comment")
        if type(lines) is str:
            return report(1, "lines", False,
                          "lines is one big string, not a list. Add .splitlines() at the end")
        if type(lines) is list and len(lines) > 0 and lines[0].endswith("\n"):
            return report(1, "lines", False,
                          "each line still ends with a newline. Use .read().splitlines() "
                          "instead of .readlines()")
        if type(lines) is list and len(lines) > 0 and lines[-1] == "":
            return report(1, "lines", False,
                          "there is an extra empty string at the end of the list. "
                          "Use .splitlines() instead of .split(...)")
        if type(lines) is list:
            return report(1, "lines", False,
                          f"expected a list of {len(expected)} lines, got a list of {len(lines)}. "
                          "Use open(LOG_FILE).read().splitlines()")
        return report(1, "lines", False,
                      f"expected a list of {len(expected)} lines, got a {type(lines).__name__}. "
                      "Use open(LOG_FILE).read().splitlines()")
    except Exception as error:
        return report(1, "lines", False, f"checker error: {error}")


def check_task_2_fails():
    try:
        expected = expected_fails()
        if type(fails) is dict and fails == expected:
            return report(2, "fails", True)
        if len(fails) == 0:
            return report(2, "fails", False,
                          "fails is empty. Finish Task 1 first so the loop has lines to read")
        if None in fails:
            return report(2, "fails", False,
                          "fails has None as a key. Fill in ip (Task 2a) with line.split()[-4]")
        if None in fails.values():
            return report(2, "fails", False,
                          "some counts are None. Fill in new_count (Task 2b)")
        if set(fails) != set(expected):
            return report(2, "fails", False,
                          "the keys are not the right IPs. The IP is the 4th word from "
                          "the end: line.split()[-4]")
        if set(fails.values()) == {1}:
            return report(2, "fails", False,
                          "every count is 1. Add one to the OLD count: fails.get(ip, 0) + 1")
        return report(2, "fails", False,
                      f"the IPs are right but some counts are wrong (expected "
                      f"{sum(expected.values())} failures in total, got {sum(fails.values())}). "
                      "Use fails.get(ip, 0) + 1")
    except Exception as error:
        return report(2, "fails", False, f"checker error: {error}")


def check_task_3_alerts():
    try:
        expected = expected_alerts()
        # Sets of tuples let us compare without caring about order.
        if type(alerts) is list and set(alerts) == set(expected) and len(alerts) == len(expected):
            if all(type(item) is tuple for item in alerts):
                return report(3, "alerts", True)
            return report(3, "alerts", False, "each alert should be a tuple: (ip, count)")
        if len(alerts) == 0:
            return report(3, "alerts", False,
                          f"no alerts yet (expected {len(expected)}). Set is_alert to a "
                          "True/False test, and finish Task 2 first")
        if type(is_alert) is str:
            return report(3, "alerts", False,
                          "is_alert is text in quotes, so it always counts as True. "
                          "Remove the quotes so Python runs the test")
        if fails != expected_fails():
            return report(3, "alerts", False,
                          "Task 2 is not passing yet, so the counts are off. Fix Task 2 first")
        alerted = set()
        for item in alerts:
            alerted.add(item[0])
        for address, total in expected_fails().items():
            if total < THRESHOLD and address in alerted:
                return report(3, "alerts", False,
                              f"{address} has only {total} failures but was alerted. "
                              "Test count > THRESHOLD, and join the two tests with 'and' (not 'or')")
        for address in allowlist:
            if address in alerted:
                return report(3, "alerts", False,
                              f"{address} is on the allowlist and should NOT be alerted. "
                              "Add a 'not in allowlist' test")
        for address, total in expected_fails().items():
            if total == THRESHOLD and address in alerted:
                return report(3, "alerts", False,
                              f"{address} has exactly {THRESHOLD} failures. That is not MORE than "
                              f"{THRESHOLD}. Use > instead of >=")
        return report(3, "alerts", False,
                      f"expected {len(expected)} alerts, got {len(alerts)}. Check both tests: "
                      "count > THRESHOLD and ip not in allowlist")
    except Exception as error:
        return report(3, "alerts", False, f"checker error: {error}")


def check_task_4_threat_intel():
    try:
        expected = expected_threat_intel()
        if type(threat_intel) is set and threat_intel == expected:
            return report(4, "threat_intel", True)
        if threat_intel is None:
            return report(4, "threat_intel", False,
                          "got None. Read BAD_IPS_FILE like Task 1, then wrap it in set( ... )")
        if type(threat_intel) is list and set(threat_intel) == expected:
            return report(4, "threat_intel", False,
                          "the right IPs, but it is a list. Wrap it in set( ... ) for fast lookups")
        if type(threat_intel) is set and len(threat_intel) == 1:
            return report(4, "threat_intel", False,
                          "the set has only 1 item. Did you forget .splitlines()?")
        if type(threat_intel) is set and all(len(str(item)) == 1 for item in threat_intel):
            return report(4, "threat_intel", False,
                          "the set holds single characters, not IPs. "
                          "Add .splitlines() before wrapping it in set( ... )")
        if type(threat_intel) is set and any(str(item).endswith("\n") for item in threat_intel):
            return report(4, "threat_intel", False,
                          "the IPs still end with a newline. Use .read().splitlines() "
                          "instead of .readlines()")
        return report(4, "threat_intel", False,
                      f"expected a set of {len(expected)} IPs. Did you read BAD_IPS_FILE "
                      "(not LOG_FILE) and use set()?")
    except Exception as error:
        return report(4, "threat_intel", False, f"checker error: {error}")


def check_task_5_confirmed():
    try:
        expected_alert_ips = set()
        for address, total in expected_alerts():
            expected_alert_ips.add(address)
        expected = expected_alert_ips & expected_threat_intel()
        if type(confirmed) is set and confirmed == expected:
            return report(5, "confirmed", True)
        if confirmed is None:
            return report(5, "confirmed", False,
                          "got None. Use & between alert_ips and threat_intel")
        if type(confirmed) is not set:
            return report(5, "confirmed", False,
                          f"confirmed should be a set, got a {type(confirmed).__name__}. "
                          "& between two sets gives you a set")
        inputs_ok = (alert_ips == expected_alert_ips
                     and type(threat_intel) is set and threat_intel == expected_threat_intel())
        if len(confirmed) == 0 and inputs_ok:
            # Usually: set(alerts) & threat_intel. Tuples never match plain IP strings.
            return report(5, "confirmed", False,
                          "the set is empty. Use alert_ips (just the IPs), "
                          "not alerts (the list of (ip, count) tuples)")
        if len(confirmed) == 0:
            return report(5, "confirmed", False,
                          "the set is empty. Are Tasks 3 and 4 passing? Both sets need to be filled")
        if confirmed == alert_ips:
            return report(5, "confirmed", False,
                          "that is every alert IP. Keep only the ones ALSO in threat_intel, using &")
        if inputs_ok and confirmed in (alert_ips - threat_intel, threat_intel - alert_ips,
                                       alert_ips | threat_intel):
            return report(5, "confirmed", False,
                          "wrong set operator. & keeps only the items in BOTH sets. "
                          "- and | do something else")
        return report(5, "confirmed", False,
                      f"expected a set of {len(expected)} IPs that are in BOTH alert_ips "
                      "and threat_intel. Use & between alert_ips and threat_intel")
    except Exception as error:
        return report(5, "confirmed", False, f"checker error: {error}")


def run_checks():
    print("=" * 50)
    print(f"Checking Lab {LAB_NUMBER}...")
    print("=" * 50)
    results = [
        check_task_1_lines(),
        check_task_2_fails(),
        check_task_3_alerts(),
        check_task_4_threat_intel(),
        check_task_5_confirmed(),
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
        print()
        print("That was the last lab. Now open a pull request (see the README).")
    else:
        print("Read the FAIL hints above, fix those tasks, and run this file again.")


run_checks()
