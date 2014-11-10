set nocompatible
source $VIMRUNTIME/vimrc_example.vim
source $VIMRUNTIME/mswin.vim
behave mswin
" 设定默认解码
set fenc=utf-8
set fencs=utf-8,usc-bom,euc-jp,gb18030,gbk,gb2312,cp936

" 侦测文件类型
filetype on

" 载入文件类型插件
filetype plugin on

" 为特定文件类型载入相关缩进文件
filetype indent on

" 带有如下符号的单词不要被换行分割
set iskeyword+=_,$,@,%,#,-

" 语法高亮
syntax on

" 设置配色方案
colorscheme habiLight

" 字符间插入的像素行数目
set linespace=0

" 在状态行上显示光标所在位置的行号和列号
set ruler
set rulerformat=%20(%2*%<%f%=\ %m%r\ %3l\ %c\ %p%%%)

" 在被分割的窗口间显示空白，便于阅读
set fillchars=vert:\ ,stl:\ ,stlnc:\


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" 搜索和匹配
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" 高亮显示匹配的括号
set showmatch

" 在搜索的时候忽略大小写
set ignorecase

" 在搜索时，输入的词句的逐字符高亮（类似firefox的搜索）
set incsearch

" 我的状态行显示的内容（包括文件类型和解码）
set statusline=%F%m%r%h%w\[POS=%l,%v][%p%%]\%{strftime(\"%d/%m/%y\ -\ %H:%M\")}

" 总是显示状态行
set laststatus=1

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" 文本格式和排版
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

" 继承前一行的缩进方式，特别适用于多行注释
set autoindent

" 显示行号
set nu

set t_Co=256

" 用空格代替制表符
set expandtab

" 制表符为4统一缩进为4
set tabstop=4
set softtabstop=4
set shiftwidth=4
