@echo on
pyinstaller -F -p "game:utils:features" --noupx "braingames.py"
cd dist
mkdir resources
xcopy "../resources" "resources"