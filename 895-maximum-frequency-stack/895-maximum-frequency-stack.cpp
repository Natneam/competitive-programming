class FreqStack {
private:
    unordered_map<int, int> freq;
    unordered_map<int, stack<int>> stacks;
    int max_freq = 0;
public:
    FreqStack() {}
    
    void push(int val) {
        max_freq = max(max_freq, ++freq[val]);
        stacks[freq[val]].push(val);
    }
    
    int pop() {
        int val = stacks[max_freq].top();
        stacks[max_freq].pop();
        freq[val]--;
        if(!stacks[max_freq].size()) max_freq--;
        return val;
    }
};

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack* obj = new FreqStack();
 * obj->push(val);
 * int param_2 = obj->pop();
 */