1. install crystax-ndk

2. change ndk location -> crystax-ndk

3. edit python script, put it into assets

4. edit pybridge.c, add the native function

5. call it in java (PyBridge.java and MainAty)

6. terminal cd into jni dir, run path\to\crystax-ndk ndk-build

7. rename the output libs to jniLibs

8. run it!!
