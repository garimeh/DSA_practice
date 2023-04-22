template <typename T>

class queue_arr{
    int size;
    int head;
    int tail;
    T * data;
    int cap;

    public:
    queue_arr(int s){
        size = 0;
        head = -1;
        tail = 0;
        data = new T(s);
        cap = s;
    }

    int getSize(){
        return size;
    }

    bool isEmpty(){
        return size == 0;
    }

    void enqueue(T e){
        if(size == cap){
            cout<<"Queue full! "<<endl;
            return;
        }
        data[tail] = e;
        tail = (tail+1)%cap;
        if(head == -1){
            head = 0;
        }
        size++;
    }

    T front(){
        if(isEmpty()){
            cout<<" Queue is empty"<<endl;
            return 0;
        }
        return data[head];
    }

    T dequeue(){
        if(isEmpty()){
            cout<<"Queue is empty!"<<endl;
            return 0;
        }
        T temp = data[head];
        head = (head + 1)% cap;
        size--;
        if(size == 0){
            head = -1;
            tail = 0;
        }
        return temp;
    }
  
};