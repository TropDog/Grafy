# Workflows

This project uses **GitHub Actions** to automate continuous integration (CI) and continuous deployment (CD) processes. Below is a detailed description of the workflow used in the project.

---

## Workflow: Python Tests and Linting

The workflow is defined in the `.github/workflows` directory as a YAML file. It is triggered on:

- **Push events** to the `dev` and `main` branches.
- **Pull requests** targeting the `dev` and `main` branches.

### **Trigger Conditions**

| Event        | Branches    |
|--------------|-------------|
| `push`       | `dev`, `main` |
| `pull_request` | `dev`, `main` |

---

## 🛠️ **Jobs in the Workflow**

### **Job: Lint and Test**

The workflow runs a single job called `lint-and-test` on an **Ubuntu virtual machine** (`ubuntu-latest`).

### **Steps in the Job**

#### **Step 1: Checkout Code**

This step uses the `actions/checkout` action to clone the repository into the runner.

```yaml
- name: Checkout code
  uses: actions/checkout@v3