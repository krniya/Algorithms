class interNode{
    public:
    interNode* left;
    interNode* right;
    int tl,tr,v,ly;
    interNode(int l, int r){
        v = 0;
        ly = 0;
        left = NULL;
        right = NULL;
        tl = l;
        tr = r;
    }
    
    void add(){
        int t = (this->tl + this->tr)/2;
        if(this->left == NULL || this->right == NULL){
            this->left = new interNode(this->tl,t);
            this->right = new interNode(t+1,this->tr);
        }
        
        if(this->ly){
            this->left->ly = 1;
            this->right->ly = 1;
            this->left->v = t - this->tl + 1;
            this->right->v = this->tr - (t+1) + 1;
            this->ly = 0;
        }
    }
    
    int search(int l, int r){
        if(l>r || r<this->tl || l>this->tr) return 0;
        if( l<= this->tl && r>= this->tr) return this->v;
        this->add();
        int res = 0;
        if(this->left != NULL) res += this->left->search(l,r);
        if(this->right != NULL) res += this->right->search(l,r);
        return res;
    }
    
    void insert(int l, int r){
        if(l>r || r<this->tl || l>this->tr) return;
        if( l<= this->tl && r>= this->tr){
            this->v = this->tr-this->tl+1;
            this->ly = 1;
            return;
        }
        this->add();
        if(this->left != NULL)
        this->left->insert(l,r);
        if(this->right != NULL)
        this->right->insert(l,r);
        this->v = 0;
        if(this->left != NULL) this->v += this->left->v;
        if(this->right != NULL) this->v += this->right->v;
    }
};

class CountIntervals {
public:
    interNode* node;
    CountIntervals() {
        node = new interNode(1,1000000000);
    }
    
    void add(int left, int right) {
        node->insert(left,right);
    }
    
    int count() {
        return node->search(1,1000000000);
    }
};

/**
 * Your CountIntervals object will be instantiated and called as such:
 * CountIntervals* obj = new CountIntervals();
 * obj->add(left,right);
 * int param_2 = obj->count();
 */