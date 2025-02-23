# Demo of [Defect](https://github.com/DiscreteTom/defect)

## Setup

```bash
# download defect binary
wget https://github.com/DiscreteTom/defect/releases/latest/download/defect

# setup pre-commit git hook
cp ./script/pre-commit .git/hooks
chmod +x .git/hooks/pre-commit
```

## Test

### Git Hook

```bash
# undo the last commit
git reset HEAD~
# re-add all changes
git add .
# re-commit, this should trigger the git hook
git commit -C ORIG_HEAD
```
