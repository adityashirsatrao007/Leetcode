// Last updated: 6/4/2025, 9:18:30 PM
class Solution {
        public int[] closestPrimes(int left, int right) {
                int a=-1, b=-1;
                        List<Integer> prime=new ArrayList();

                                for(int p=left; p<=right; p++){
                                            if(primeVal(p)){
                                                            // if prime like [2,3], [5,7], [11,13], [17,19] and so on ... found return immediately
                                                                            if(prime.size()>=1 && p<=prime.get(prime.size()-1)+2){
                                                                                                return new int[]{prime.get(prime.size()-1),p};
                                                                                                                }
                                                                                                                                prime.add(p);
                                                                                                                                            }
                                                                                                                                                    }
                                                                                                                                                            

                                                                                                                                                                    if(prime.size()<2){
                                                                                                                                                                                return new int[]{a,b};
                                                                                                                                                                                        }

                                                                                                                                                                                                int minVal=Integer.MAX_VALUE;
                                                                                                                                                                                                        for(int i=1; i<prime.size(); i++){
                                                                                                                                                                                                                    if(minVal>prime.get(i)-prime.get(i-1)){
                                                                                                                                                                                                                                    minVal=prime.get(i)-prime.get(i-1);
                                                                                                                                                                                                                                                    a=prime.get(i-1);
                                                                                                                                                                                                                                                                    b=prime.get(i);
                                                                                                                                                                                                                                                                                }
                                                                                                                                                                                                                                                                                        }

                                                                                                                                                                                                                                                                                                return new int[]{a,b};
                                                                                                                                                                                                                                                                                                    }

                                                                                                                                                                                                                                                                                                        boolean primeVal(int val){     
                                                                                                                                                                                                                                                                                                                if(val==1) return false;  
                                                                                                                                                                                                                                                                                                                        else if(val==2) return true; 
                                                                                                                                                                                                                                                                                                                                for(int i=2; i<Math.sqrt(val)+1; i++){
                                                                                                                                                                                                                                                                                                                                            if(val%i==0){
                                                                                                                                                                                                                                                                                                                                                            return false;
                                                                                                                                                                                                                                                                                                                                                                        }
                                                                                                                                                                                                                                                                                                                                                                                }
                                                                                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                return true;
                                                                                                                                                                                                                                                                                                                                                                                                    }

                                                                                                                                                                                                                                                                                                                                                                                                    }




