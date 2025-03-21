# Demo of [Defect](https://github.com/DiscreteTom/defect)

In this demo we will use `defect` with AWS Bedrock LLMs to review code.

> [!NOTE]
> The prompt used in this demo will more likely to give suggestions, which might be annoying. In real world, you should modify the prompt to only check for the specific issues you care about.

## Git Hook

### Setup

Making sure you are running on a Linux x86_64 environment, and have AWS credentials set.

```bash
# download defect binary
wget https://github.com/DiscreteTom/defect/releases/download/v0.3.3/defect-v0.3.3-x86_64-unknown-linux-musl.zip
unzip defect-v0.3.3-x86_64-unknown-linux-musl.zip
rm defect-v0.3.3-x86_64-unknown-linux-musl.zip
chmod +x defect

# setup pre-commit git hook
cp ./scripts/pre-commit .git/hooks
chmod +x .git/hooks/pre-commit
```

Save the following code to a file, e.g. `bad.py`.

```python
def DoStuff(x, y, z):
    a = []
    for i in range(len(x)):
        if x[i] > 10:
            temp = x[i] * y
        else:
            temp = x[i] + y
        if temp > 20:
            a.append(temp)
        if z == True:
            print("value is:" + str(temp))
    return a


def process_data():
    l = [1, 2, 3, 4, 5, 11, 12, 13]
    result = DoStuff(l, 5, True)
    for i in range(0, len(result)):
        result[i] = result[i] + 10
    return result


print(process_data())
```

Commit the change:

```bash
git add .
git commit -m "test"
```

`git` should reject the commit with suggestions printed.

## GitHub Actions

See the [`.github/workflows/`](./.github/workflows/) folder for the workflow files.

See the [GitHub Actions](https://github.com/DiscreteTom/defect-demo/actions) page for workflow runs.

The workflow has AWS credentials set according to [this blog](https://aws.amazon.com/blogs/security/use-iam-roles-to-connect-github-actions-to-actions-in-aws/).
