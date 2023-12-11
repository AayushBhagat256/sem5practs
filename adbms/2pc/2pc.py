import time
import random

def prepare_participant(participant):
    print(f"{participant}: Prepare phase")
    time.sleep(random.uniform(0.5, 1.5))
    return True

def commit_participant(participant):
    print(f"{participant}: Commit phase")
    time.sleep(random.uniform(0.5, 1.5))

def abort_participant(participant):
    print(f"{participant}: Abort phase")
    time.sleep(random.uniform(0.5, 1.5))

def send_prepare(participants):
    votes = []
    for participant in participants:
        try:
            vote = prepare_participant(participant)
            votes.append(vote)
        except Exception as e:
            print(f"Error during prepare phase: {str(e)}")
            send_abort(participants)
    if all(votes):
        send_commit(participants)
    else:
        send_abort(participants)

def send_commit(participants):
    for participant in participants:
        try:
            commit_participant(participant)
        except Exception as e:
            print(f"Error during commit phase: {str(e)}")
            send_abort(participants)

def send_abort(participants):
    for participant in participants:
        try:
            abort_participant(participant)
        except Exception as e:
            print(f"Error during abort phase: {str(e)}")

if __name__ == "__main__":
    participant1 = "Participant 1"
    participant2 = "Participant 2"

    participants = [participant1, participant2]

    try:
        send_prepare(participants)

        print("Transaction committed successfully!")

    except Exception as e:
        print(f"Transaction aborted: {str(e)}")
