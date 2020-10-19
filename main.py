
def search(nums, target):
  pivot=-1
  for i in range(1,len(nums)):
      if nums[i-1]>nums[i]:
          pivot = i-1
          break
      
  if pivot==-1:
      start=0
      end=len(nums)
      mid=(start+end)//2
      for i in range(end):
          if target>nums[mid]:
              start=mid
              mid=(start+end)//2
          elif target<nums[mid]:
              end=mid
              mid=(start+end)//2
          else:
              return mid
      return -1
  elif target<=nums[-1]:
      start=pivot
      end=len(nums)
      mid=(start+end)//2
      for i in range(end-start):
          if target>nums[mid]:
              start=mid
              mid=(start+end)//2
          elif target<nums[mid]:
              end=mid
              mid=(start+end)//2
          else:
              return mid
      return -1
  else:
      start=0
      end=pivot+1
      mid=(start+end)//2
      for i in range(end):
          if target>nums[mid]:
              start=mid
              mid=(start+end)//2
          elif target<nums[mid]:
              end=mid
              mid=(start+end)//2
          else:
              return mid
      return -1
      
      