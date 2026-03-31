# SSEPy New Execution Flow

This file describes the updated execution flow for the current SSEPy prototype, including the new encrypted document upload step.

## Prerequisites

- Python 3.8+
- Install dependencies:
  ```bash
  pip3 install -r requirements.txt
  ```

## Start the server

Open one terminal and run:

```bash
python3 run_server.py start
```

## Client actions

Use a second terminal to perform the following steps.

### 1. Generate Config File

```bash
python3 run_client.py generate-config --scheme <scheme_name> --save-path <config.json>
```

### 2. Create a service

```bash
python3 run_client.py create-service --config <config.json> --sname <service_name>
```

### 3. Upload configuration file

```bash
python3 run_client.py upload-config --sname <service_name>
```

### 4. Create SSE Key

```bash
python3 run_client.py generate-key --sname <service_name>
```

### 5. Generate Encrypted Database

```bash
python3 run_client.py encrypt-database --sname <service_name> --db-path <db.json>
```

### 6. Upload Encrypted Database

```bash
python3 run_client.py upload-encrypted-database --sname <service_name>
```

### 7. Encrypt Document Contents

Prepare a JSON file containing documents in the form:

```json
{
  "doc1": "text of document 1",
  "doc2": "text of document 2"
}
```

The command also accepts document values as a list of strings, which are joined with newlines before encryption.

Then run:

```bash
python3 run_client.py encrypt-documents --sname <service_name> --doc-path <docs.json>
```

### 8. Upload Encrypted Document Ciphertexts to Server

```bash
python3 run_client.py upload-ciphertexts --sname <service_name>
```

At this time, the server receives the ciphertext documents and prints the received ciphertext metadata.

### 9. Delete a Service

```bash
python3 run_client.py delete_service --sname <service_name>
```

This will remove your local client service data and the service alias mapping. It also attempts to send a delete request to the server, but server-side cleanup is only available when the service has been uploaded and the connection is active.

### 10. Keyword Search

```bash
python3 run_client.py search --sname <service_name> --keyword <keyword>
```

### 11. Service Delete

```bash
python3 run_client.py delete-service --sname <service_name>
```

This Function does not completed, because it would stuck. But it still can work.

## Push this version to GitHub and create a new branch

From your Codespace terminal, use:

```bash
# Create a new branch for this work
git checkout -b feature/encrypted-documents

# Add any modified files
git add .

# Commit the changes
git commit -m "Add encrypted document upload flow and README_NEW"

# Push the branch to GitHub
git push -u origin feature/encrypted-documents
```

## Open a pull request

If you have GitHub CLI installed, you can create a PR from Codespace:

```bash
gh pr create --title "Add encrypted document upload flow" --body "Add README_NEW and encrypted document upload support" --base master --head feature/encrypted-documents
```

If you do not have `gh`, open the PR from the GitHub website by visiting the repository and selecting the new branch.
