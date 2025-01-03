import { readArticle } from "@/app/usecase/readArticle";
import Markdown from "react-markdown";
import remarkGfm from 'remark-gfm';

const BlogArticlePage = async ({ params }: { params: { id: string } }) => {
  const { id } = await params;

  // 非同期関数から記事を取得
  const article = await readArticle(id);

  // 記事のデータとコンテンツを取得
  const { data, content } = article;

  // contentを文字列に結合
  const singleContent = Array.isArray(content) ? content.join("") : content;

  return (
    <div>
      <h1>{data.title}</h1>
      <Markdown remarkPlugins={[remarkGfm]}>{singleContent}</Markdown>
      </div>
  );
};

export default BlogArticlePage;