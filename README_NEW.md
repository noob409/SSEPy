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
python3 run_client.py generate_config --scheme <scheme_name> --save-path <config.json>
```

### 2. Create a service

```bash
python3 run_client.py create_service --config <config.json> --sname <service_name>
```

### 3. Upload configuration file

```bash
python3 run_client.py upload_config --sname <service_name>
```

### 4. Create SSE Key

```bash
python3 run_client.py generate_key --sname <service_name>
```

### 5. Generate Encrypted Database

```bash
python3 run_client.py encrypt_database --sname <service_name> --db-path <db.json>
```

### 6. Upload Encrypted Database

```bash
python3 run_client.py upload_encrypted_database --sname <service_name>
```

### 7. Encrypt Document Contents

Prepare a JSON file containing documents in the form:

```json
{
  "doc1": "text of document 1",
  "doc2": "text of document 2"
}
```

Then run:

```bash
python3 run_client.py encrypt_documents --sname <service_name> --doc-path <docs.json>
```

### 8. Upload Encrypted Document Ciphertexts to Server

```bash
python3 run_client.py upload_ciphertexts --sname <service_name>
```

At this time, the server receives the ciphertext documents and prints the received ciphertext metadata.

### 9. Keyword Search

```bash
python3 run_client.py search --sname <service_name> --keyword <keyword>
```

## Push this version to GitHub and create a new branch

From your Codespace terminal, use:

```bash
# Create a new branch for this work
git checkout -b feature/encrypted-documents

# Add the new README and any other modified files
git add README_NEW.md

git add frontend/client/commands.py frontend/client/services/service.py frontend/common/constants.py frontend/server/services/service.py frontend/client/services/file_manager.py run_client.py

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
